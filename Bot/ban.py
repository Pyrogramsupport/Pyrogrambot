from Bot import app
from pyrogram import filters

@app.on_message(filters.command("ban") & filters.group)
async def ban_cmd(client, message):
# Ban chat member forever
    await app.ban_chat_member(chat_id, user_id)
