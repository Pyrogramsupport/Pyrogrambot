from pyrogram import Client, filters
from pyrogram.types import Message





@Client.on_message(filters.private & filters.command("info"))
async def info_cmd(client, message):
    info_text=f""" <u>ᴜsᴇʀ ɪɴғᴏ </u>

<b>ғɪʀsᴛ ɴᴀᴍᴇ =</b> {message.from_user.first_name}.
<b>ʟᴀsᴛ ɴᴀᴍᴇ =</b> {message.from_user.last_name}.    
<b>ᴜsᴇʀ ɪᴅ =</b> {message.from_user.id}.          
<b>ᴜsᴇʀ ɴᴀᴍᴇ =</b> {message.from_user.username} 
<b>ᴜsᴇʀ ʟɪɴᴋ =</b> {message.from_user.mention}.                                       
"""
    await message.reply_text(info_text)
    print("User Info Successfully sent to the user")







