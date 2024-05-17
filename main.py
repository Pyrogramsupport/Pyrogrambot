from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




API_ID = "19042248"
API_HASH = "a1d443cb79941a89c493f22abf4f84cb"
BOT_TOKEN = "7065912334:AAGPjkf_nHW-I7DOrCVZResEFQJNcfBdJ1k"

Siva = Client(
    name="telegrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

PM_START = """Hello.....!, I am Siva the boss robot.
Bot is under maintenance, Still wait for new features.
"""

    
@Siva.on_message(filters.command("start"))
async def start_cmd(client, message):
    print("Start Command is working")
    await message.reply_photo(
        photo = "https://telegra.ph/file/58adbfdd00ad008e2e62b.jpg",
        caption=PM_START
    )

















print("Bot is Alive and Perfectly Working")




Siva.run()










