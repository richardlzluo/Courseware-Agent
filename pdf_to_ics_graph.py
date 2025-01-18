
from dotenv import load_dotenv
import base64
import io
import fitz
from PIL import Image
import os

import datetime
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import MessagesState, START, END, StateGraph
from langsmith import traceable


from pydantic import BaseModel, Field 
from typing import List, Optional

from icalendar import Calendar, Event

load_dotenv()

def pdf_to_base64_images(pdf_path: str):
    pdf_document = fitz.open(pdf_path)
    images_base64 = []
    
    for page_number in range(len(pdf_document)):  # Iterate through all pages
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        images_base64.append(base64.b64encode(buffer.getvalue()).decode("utf-8"))
    
    pdf_document.close()
    return images_base64


title_description = """
The format should contain the following informations:
1.The course code
2.The assignment type
3.The assignment number(if any, the number should start with a #)

For example:
TIMG 5003 -- Assignment #2
TIMG 5303 -- Exam #1A
TIMG 5103 -- Quiz
ITEC 3903 -- Take Home Exam
SCMP 5409B -- Final Exam 
"""

class ScheduleEntry(BaseModel):
    title: str = Field(description=title_description)
    description: str = Field(description="A brief description of the schedule entry in no more than five sentences")
    date: datetime.date = Field(description="The date of the schedule entry.")
    time: datetime.time = Field(description="The time of the schedule entry. If no time is specified in the document, just use 23:59:59 as the time.")

class Schedule(BaseModel):
    has_schedule: bool = Field(description="Does the document have a schedule?")
    follow_up: str = Field(description="Follow up message to inform the user to upload another file.")
    schedule: List[ScheduleEntry] = Field(description="A list of schedule entries.")

llm = ChatOpenAI(model=os.getenv("chatGPT_model"), temperature=0) 

SYSTEM_PROMPT = """
You will be given a document that is the outline of a course. 
Read through the document and extract the submission time of each assignment, exam, homework, or something like these. 
Try your best to extract the title, the specific tasks, and the most importantly, the date and time of the submission time. 
The submission time should be returned as a date and a time seperately.
Fill the schedule property in to output as true and generate a list of schedule entries. 
If the whole schedule is not available, just fill the has_schedule property in to output as false and generate a follow up message to inform the user to upload another file and fill it in the follow_up property. 
"""

@traceable
def extract_calendar(state: MessagesState):
    generation_instructions = SystemMessage(content=SYSTEM_PROMPT)
    messages = [generation_instructions, state["messages"][-1]]
    structured_llm = llm.with_structured_output(Schedule, method="function_calling")
    result = structured_llm.invoke(messages)
    return {"messages": AIMessage(content=[{"result": result}])}



def get_graph():
    builder = StateGraph(MessagesState)
    builder.add_node("extract_calendar", extract_calendar)
    builder.add_edge(START, "extract_calendar")
    builder.add_edge("extract_calendar", END)
    graph = builder.compile()

    print("graph compiled") 
    return graph

def get_calendar(schedule):
    cal = Calendar()
    cal.add('prodid', '-//Richard Luo//Courseware-to-ICS//')
    for schedule_entry in schedule:
        event = Event()
        event.add('summary', schedule_entry.title)
        event.add('description', schedule_entry.description)
        event.add('dtstart', datetime.datetime.combine(schedule_entry.date, schedule_entry.time))
        event.add('dtend', datetime.datetime.combine(schedule_entry.date, schedule_entry.time))
        event.add('dtstamp', datetime.datetime.now())
        cal.add_component(event)
    
    return cal
