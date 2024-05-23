from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random 

funList = ["Who decided that? - Lelouch Lamperouge, Code Geass",
           "I'll be the hero! - Izuku Midoriya, My Hero Academia",
           "See you later, Space Cowboy. - Spike Spiegel, Cowboy Bebop",
           "I'll do it because I want to, not because I have to. - Yagami Light, Death Note",
           "The dreams of yesterday are the hopes of today and the reality of tomorrow." - Miyamoto Musashi, Vagabond"
           
          
]



@Client.on_message(filters.command("aq"))
async def aq_cmd(client, message):
    await message.reply_text(
        text=random.choice(funList)
    )
