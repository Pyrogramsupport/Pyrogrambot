#Import the libs
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import asyncio

#create env

API_ID = "19042248"
API_HASH = "a1d443cb79941a89c493f22abf4f84cb"
BOT_TOKEN = "7065912334:AAGPjkf_nHW-I7DOrCVZResEFQJNcfBdJ1k"

#create client

Siva = Client(
    name="telegrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


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
    
@Siva.on_message(filters.command("start"))
async def start_cmd(client, message):
    print("Start Command is working")
    reply1 = await message.reply_text("Loading")
    await asyncio.sleep(0.9)
    reply2 = await message.edit("Loading.")
    await asyncio.sleep(0.9)
    reply3 = await message.edit("Loading..")
    await asyncio.sleep(0.9)
    reply4 = await message.edit("Loading...")
    await asyncio.sleep(0.9)
    await reply4.delete()
    await message.reply_photo(
        photo = "https://telegra.ph/file/58adbfdd00ad008e2e62b.jpg",
        caption=PM_START,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
















print("Bot is Alive and Perfectly Working")




Siva.run()










