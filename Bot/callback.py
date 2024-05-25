from Bot import app
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
import script


@app.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "info":
        await msg.message.edit(
            text = "/info :- get user info ",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("🔙 Back", callback_data="help_back")
                ]]
            )
        )
    elif msg.data == "help_back":
        await msg.message.edit(
            text=script.HELP_TEXT,
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("Info", callback_data="info")
                ]]
            )
        )
          
  
