from Bot import app
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
import script


@app.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "info":
        await msg.message.edit(
            text = "/info :- get user info "
        )
          
  
