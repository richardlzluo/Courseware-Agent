
from config import Config

import logging
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, CallbackContext
import threading
import uuid
import time
from pdf_to_ics_graph import *
import base64
from PIL import Image
from io import BytesIO
import asyncio

graph = get_graph()


def show_images(base64_images):
    for base64_image in base64_images:
        image_data = base64.b64decode(base64_image)
        image = Image.open(BytesIO(image_data))
        image.show()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

greeting = """
Hi there\! I'm here to help you generate a calendar🗓️ for your assignments📝 and exams from a course outline, which you can import into your devices\. Please send me your course outline as a PDF file\.

__*Be cautious*__:
\* I just accept PDF files, don't send me anything else\.
\* I will return a \.ics file, which is a calendar file\. Use a PC or Mac🖥️ to import it\. Do not use an iPhone 📵\. It doesn't work with \.ics file\. You can synch it into you iPhone using iCloud or send the \.ics file through an email\. iPhone work with \.ics file in the Mail app\. You may also try it on an Ardoid phone\. I don't know if it works\.
\* Currently, I can only finish this single task, don't even try to instruct me to do anything else\. I won't response🤷‍♂️\. 
\* Use the outcome with the __*utmost caution*__\.The calendar is generated using an LLM\. I can't guarantee the accuracy\. Please *double check* it yourself\.
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=greeting, parse_mode="MarkdownV2")
    
async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    """Handle PDF file uploads."""
    file = update.message.document
    #global should_finish_typing 
    
    
    if file.mime_type == 'application/pdf':
        file_id = file.file_id
        file_name = file.file_name

        new_file = await context.bot.get_file(file_id)
        new_file_name = f"file_{int(time.time())}_{uuid.uuid4().hex}.pdf"
        await new_file.download_to_drive(f"./cache/{new_file_name}")
        await update.message.reply_text(f"Your PDF file has been accepted. Please give me a second to process it⏳...")
        
        await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)

        
        base64_images = pdf_to_base64_images(Config.cache_dir+new_file_name)
        os.remove(Config.cache_dir+new_file_name)
        messages = [HumanMessage(
                        content=[
                            {
                                "type": "image_url",
                                "image_url": {"url": f"data:image/jpeg;base64,{image}"}
                            } for image in base64_images
                        ]
                    )]

        result = graph.invoke({"messages": messages})
        
        if result["messages"][-1].content[0]['result'].has_schedule:
            schedule = result["messages"][-1].content[0]['result'].schedule
            cal = get_calendar(schedule)
            ics_file_name = f"assignment_schedule_{int(time.time())}_{uuid.uuid4().hex}.ics"
            with open(Config.cache_dir+ics_file_name, 'wb') as f:
                f.write(cal.to_ical())
                
            
            try:
                with open(Config.cache_dir+ics_file_name, 'rb') as file:
                    await update.message.reply_text("Here is your calendar file:")
                    await context.bot.send_document(
                        chat_id=chat_id,
                        document=file,
                        filename="Assignment Schedule.ics"
                    )
            except FileNotFoundError:
                await update.message.reply_text("File not found. Please check the file path.")
            except Exception as e:
                await update.message.reply_text(f"An error occurred: {e}")    
        else:
            await update.message.reply_text("This file does have a schedule for assignments or exams on it. Please try another one.")
                
    else:
        await update.message.reply_text("The file you sent is not a PDF. Please send a valid PDF file.")


if __name__ == '__main__':
    application = ApplicationBuilder().token(Config.telegram_bot_token).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.Document.MimeType("application/pdf"), handle_pdf))
    
    application.run_polling()
    
    