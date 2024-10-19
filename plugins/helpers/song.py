from HorridAPI import Songmrz 
import os
from info import HORRI_API_KEY
from pyrogram import Client, filters
import aiohttp

api_key = HORRI_API_KEY

Horrid = Songmrz(api_key)

@Client.on_message(filters.command("song"))
async def song(client, message):
    if len(message.command) < 2:  # Changed to message.command to properly check for command arguments
        await message.reply("Give An Any Song Name!")
        return

    query = " ".join(message.command[1:])  
    m = await message.reply_text("**📥 Downloading...**")

    try:
        data = Horrid.download(query)  # Ensure this line doesn't throw an error (handle exceptions if necessary)
        url = data.url
        thumb_url = data.thumb
        title = data.title
        dura = data.duration
        songs = f"Title: {title}\nDuration: {dura}\nProvided by @Mrz_bots"

        await m.edit("**📤 Uploading...**") 
        await message.reply_photo(photo=thumb_url, caption=songs)

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                with open(f"{title}.mp3", "wb") as f:
                    f.write(await resp.read())  # Use await resp.read() instead of await resp.content.read()
            async with session.get(thumb_url) as resp:
                with open("thumb.jpg", "wb") as f:
                    f.write(await resp.read())  # Same change here

        await message.reply_audio(f"{title}.mp3", thumb="thumb.jpg", title=title, caption=songs)
    except Exception as e:
        await m.edit("An error occurred while processing your request.")
        print(f"Error: {e}")  # Log the error for debugging

    await m.delete()
