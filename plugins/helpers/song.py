# credit by @Mrz_bots

from HorridAPI import api
import os
from pyrogram import Client, filters
import aiohttp

@Client.on_message(filters.command("song"))
async def song(client, message):
    if len(message.text.split()) < 2:
        await message.reply("Give An Any Song Name!")
        return

    query = " ".join(message.command[1:])    
    data = api.song(query)
    m = await message.reply_text("**📥 Downloading...**")
    url = data['url']
    thumb_url = data['thumb']
    title = data['title']
    dura = data['duration']
    songs = f"Title: {title}\nDuration: {dura}\nProvide by @Mrz_bots"
    await m.edit("**📤 Uploading...**") 
    await message.reply_photo(photo=thumb_url, caption=songs)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(f"{title}.mp3", "wb") as f:
                f.write(await resp.content.read())
        async with session.get(thumb_url) as resp:
            with open("thumb.jpg", "wb") as f:
                f.write(await resp.content.read())
    await message.reply_audio(f"{title}.mp3", thumb="thumb.jpg", title=title, caption=songs)
    await m.delete()
