
import os

class Config():
    # Replace with your bot token and channel ID
    telegram_bot_token = '7586563989:AAG5wlhJ2Qy2FmKdp9RNO6yl-CEfpTEhCsU'
    telegram_channel_id = '@raven_agent_bot'  # Use '@ChannelUsername' or numeric ID (e.g., -1001234567890)
    chatGPT_model = 'gpt-4o-mini'
    
    cache_dir = './cache/'
    working_dir = './working/'

os.environ["OPENAI_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["TAVILY_API_KEY"] = "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"
os.environ["LANGCHAIN_PROJECT"] = "courseware-ics"

# Hello world