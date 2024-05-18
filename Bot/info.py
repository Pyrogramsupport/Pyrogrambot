from pyrogram import Client, filters
from pyrogram.types import Message





@Client.on_message(filters.command("info"))
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

#ɪɴғᴏ ɪɴ ᴄʜᴀᴛ
@Client.on_message(filters.group & filters.command("info"))
async def info_cmd(client, message):
    group_text=f""" <u>ɢʀᴏᴜᴘ ɪɴғᴏ </u>

<b>ᴛɪᴛʟᴇ =</b> {message.chat.title}.
<b>ᴄʜᴀᴛ ɪᴅ =</b> {message.chat.id}.
<b>ɪɴᴠɪᴛᴇ ʟɪɴᴋ =</b> {message.chat.invite_link}.          
<b>ᴄʜᴀᴛ ɴᴀᴍᴇ =</b> {message.chat.username}                                       
"""
    await message.reply_text(info_text)
    print("User Info Successfully sent to the user")






