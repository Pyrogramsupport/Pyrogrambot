from Bot import app

if __name__ == "__main__":
    print("bot is functioning")
    app.run()
    with app:
        Siva.send_photo(
            chat_id=-1002123259805,
            photo="https://telegra.ph/file/cefe116aeebdc9462971a.jpg",
            caption="𝐵𝑜𝑡 𝑖𝑠 𝑠𝑡𝑎𝑟𝑡𝑒𝑑 𝑡𝑜 𝑤𝑜𝑟𝑘𝑖𝑛𝑔"
        )
