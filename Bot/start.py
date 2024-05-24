from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
from Bot import app


@app.on_message(filters.command("start") & filters.group)
async def start_cmd(client, msg):
    reply1 = await msg.reply_text("**please wait**")
    await asyncio.sleep(1)
    reply2 = await reply1.edit("`opening`")
    await asyncio.sleep(0.7)
    await reply2.edit(
        photo="https://telegra.ph/file/58adbfdd00ad008e2e62b.jpg",
        caption="**Click the below button**",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Open in private", url="https://t.me/Sivatheboss_x_robot")
            ]]
        )
    )
  
