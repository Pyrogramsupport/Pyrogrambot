import asyncio
from pyrogram import Client

async def main():
Siva = Client(
    "Pyrogrambot",
    api_id="19042248",
    api_hash="a1d443cb79941a89c493f22abf4f84cb",
    bot_token="7065912334:AAH-po3qWn85LJXgre0qni4waQgQ3sjsv1g",
    plugins=dict(root="Bot")
)

print("Bot is started and perfectly working ")
    async with Siva: 
        await Siva.send_photo(
            chat_id=-1002123259805,
            photo="https://telegra.ph/file/cefe116aeebdc9462971a.jpg",
            caption="𝐵𝑜𝑡 𝑖𝑠 𝑠𝑡𝑎𝑟𝑡𝑒𝑑 𝑡𝑜 𝑤𝑜𝑟𝑘𝑖𝑛𝑔"
        )
asyncio.run(main())
