from Bot import app
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
import script


@app.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "info":
        await msg.message.edit(
            text = "Info usage \n• /info :- get user info. \n• /ginfo :- Gets group info.",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("🔙 Back", callback_data="help_back")
                ]]
            )
        )
    elif msg.data == "help_back":
        await msg.message.edit(
            text=script.HELP_TEXT,
            reply_markup=InlineKeyboardMarkup(script.HELP_BUTTON)
                
    elif msg.data == "day":
        await msg.message.edit(
            text = "**CLICK ** == `morning` , `evening` , `afternoon` , `night` :- use this words wait and see.",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("🔙 Back", callback_data="help_back")
                ]]
            )
        )
    elif msg.data == "logo":
        await msg.message.edit(
            text = "_______________________\n    **Logo**     \n____________________\n• /logo = generate a logo.\n**Note :-** 1. If you reply a image make a logo that image.\n      2. If you not reply a img don't worry, it take random image.\n Ex :- /logo Siva",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("🔙 Back", callback_data="help_back")
                ]]
            )
    )
          
  
