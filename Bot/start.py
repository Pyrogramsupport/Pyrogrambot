from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
from Bot import app

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
 
@app.on_message(filters.command("start") & filters.private)
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
  
