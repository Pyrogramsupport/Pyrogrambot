from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from Bot import app
import script 

@app.on_message(filters.command("help"))
async def help_cmd(client, msg):
    await msg.reply_text(
        text = script.HELP_TEXT,
        reply_markup = InlineKeyboardMarkup(
            [[
                  InlineKeyboardButton("Info", callback_data="info")
            ]]
        )
    )
    
