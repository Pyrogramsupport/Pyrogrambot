from pyrogram import Client, emoji, filters
from Bot import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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



if __name__ == "__main__":
    print("bot is functioning")
    app.run()
    with app:
        app.send_photo(
            chat_id=-1002054576768,
            photo="https://telegra.ph/file/cefe116aeebdc9462971a.jpg",
            caption="𝐵𝑜𝑡 𝑖𝑠 𝑠𝑡𝑎𝑟𝑡𝑒𝑑 𝑡𝑜 𝑤𝑜𝑟𝑘𝑖𝑛𝑔",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("ADD ME TO YOUR GROUP", url = "https://t.me/sivatheboss_x_robot?startgroup=True")
                ]]
            )
        )
