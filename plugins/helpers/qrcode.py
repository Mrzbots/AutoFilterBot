from pyrogram import Client, filters
from HorridAPI import api

@Client.on_message(filters.command("qr"))
async def qrcode(bot, message):
    if len(message.command) > 1:
        text = ' '.join(message.command[1:])
        client = api.qr(text)
        await message.reply_photo(client)
    else:
        await message.reply("provide a query, like /qr hi")
