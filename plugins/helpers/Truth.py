# provide by HorridAPI 

from pyrogram import Client, filters
from HorridAPI import api

@Client.on_message(filters.command("joke"))
async def joke_command(client, message):
    await message.reply_text(api.joke())

@Client.on_message(filters.command("truth"))
async def truth_command(client, message):
    await message.reply_text(api.truth())

@Client.on_message(filters.command("dare"))
async def dare_command(client, message):
    await message.reply_text(api.dare())
