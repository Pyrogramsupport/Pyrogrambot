from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random 

funList = ["add soon"]



@Client.on_message(filters.command("aq"))
async def aq_cmd(client, message):
    await message.reply_text(
        text=random.choice(funList)
    )
