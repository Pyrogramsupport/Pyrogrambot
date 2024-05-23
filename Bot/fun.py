from program import Client, filters
from main.py import Siva
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random 

funList = ["add soon"]



@Siva.on_message(filters.command("aq"))
async def aq_cmd(client, message):
    await message.reply_text(
        text=random.choice(funList)
    )
