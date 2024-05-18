from pyrogram import Client, filters

info_text =f""" ᴜsᴇʀ ɪɴғᴏ 
________________________________________________
|| ғɪʀsᴛ ɴᴀᴍᴇ = {message.from_user.first_name}.||
|| ʟᴀsᴛ ɴᴀᴍᴇ = {message. from_user.last_name}. ||
|| ғᴜʟʟ ɴᴀᴍᴇ = {message. from_user.fullname}.  ||
|| ᴜsᴇʀ ɪᴅ = {message. from_user.id}.          ||
|| ᴜsᴇʀ ɴᴀᴍᴇ = {message.from_user.username}    ||
|| ᴜsᴇʀ ʟɪɴᴋ = {message.from_user.mention}.     ||                                      
________________________________________________
"""



@Client.on_message(filters.private & filters.command("info"))
async def info_cmd(client, message):
    await message.reply_text(info_text)
    print("User Info Successfully sent to the user")







