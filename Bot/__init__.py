from pyrogram import Client
import os
import time


api_id = 19042248
api_hash = "a1d443cb79941a89c493f22abf4f84cb"
bot_token = "7186790371:AAHT3lvITPS6JRC-7MCtIRThK3yS-NHWe7U"



app = Client(
       "MyTgBot", 
       api_id=api_id, 
       api_hash=api_hash,
       bot_token=bot_token,
       plugins=dict(root="Bot")
)
