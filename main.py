from pyrogram import Client, filters





API_ID = "19042248"
API_HASH = "a1d443cb79941a89c493f22abf4f84cb"
BOT_TOKEN = "7065912334:AAGPjkf_nHW-I7DOrCVZResEFQJNcfBdJ1k"

Siva = Client(
    name="telegrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("Bot is Alive and Perfectly Working")
Siva.run()










