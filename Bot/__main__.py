from Bot import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
