from pyrogram import Client, filters

@Client.on_message(filters.private & filters.command("info"))
async def info_cmd(client, message):
  info_text = f"""
ғɪʀsᴛ ɴᴀᴍᴇ = {message.from_user.first_name}.
ʟᴀsᴛ ɴᴀᴍᴇ = {message. from_user.last_name}.
ғᴜʟʟ ɴᴀᴍᴇ = {message. from_user.fullname}.
ᴜsᴇʀ ʟɪɴᴋ = {message. from_user.mention}.
"""
    await message.reply_text(info_text)
    print("User Info Successfully sent to the user")









