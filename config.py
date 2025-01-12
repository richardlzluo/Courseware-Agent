
import os

class Config():
    # Replace with your bot token and channel ID
    telegram_bot_token = 'REPLACE YOU TELEGRAM BOT TOKEN'
    telegram_channel_id = 'REPLACE YOU TELEGRAM CHANNEL ID'
    chatGPT_model = 'gpt-4o-mini'
    
    cache_dir = './cache/'
    working_dir = './working/'

os.environ["OPENAI_API_KEY"] = "REPLACE YOU OPENAI API KEY"
