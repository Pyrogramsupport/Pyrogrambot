#Import the libs
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import asyncio



#start cmd reply text

PM_START = """Hello.....!, I am Siva the boss robot.
Bot is under maintenance, Still wait for new features.
"""
#start cmd buttons


buttons = [[
    InlineKeyboardButton(text="Owner", url = "https://t.me/Siva_the_king")
    ],[
    InlineKeyboardButton(text="Support", url = "https://t.me/shukuranai_support")
]]



#start cmd filters 
 
@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    reply1 = await message.reply_text("`Loading `")
    await asyncio.sleep(0.9)
    reply2 = await reply1.edit("`Loading . `")
    await asyncio.sleep(0.9)
    reply3 = await reply2.edit("`Loading . . `")
    await asyncio.sleep(0.9)
    reply4 = await reply3.edit("`Loading . . . `")
    await asyncio.sleep(0.9)
    await reply4.delete()
    await asyncio.sleep(0.3)
    await message.reply_photo(
        photo = "https://telegra.ph/file/58adbfdd00ad008e2e62b.jpg",
        caption=PM_START,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    print("Start Command is working")
