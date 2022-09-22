
from pyrogram import Client
from SKY.config import Config

ID = Config.API_ID
HASH = Config.API_HASH
TK = Config.BOT_TOKEN



app = Client("SKY",api_id= ID, api_hash= HASH, bot_token= TK)

