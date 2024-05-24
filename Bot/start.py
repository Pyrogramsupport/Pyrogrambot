from pyrogram import Client, emoji, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
from Bot import app

# Target chat. Can also be a list of multiple chat ids/usernames
TARGET = -1002054576768
# Welcome message template
MESSAGE = "{} Welcome to [Pyrogram](https://t.me/siva_chat)'s group chat {}!"



# Filter in only new_chat_members updates generated in TARGET chat
@app.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def welcome(client, message):
    # Build the new members list (with mentions) by using their first_name
    new_members = [u.mention for u in message.new_chat_members]
    # Build the welcome message by using an emoji and the list we built above
    text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
    # Send the welcome message, without the web page preview
    await message.reply_text(text, disable_web_page_preview=True)







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
if len(message.text.split()) > 1 and message.text.split()[1].startswith('aq'):
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
    await reply2.delete()
    await msg.reply_photo(
        photo="https://telegra.ph/file/58adbfdd00ad008e2e62b.jpg",
        caption="**Click the below button**",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Open in private", url="https://t.me/Sivatheboss_x_robot?start=True")
            ]]
        )
    )
  
