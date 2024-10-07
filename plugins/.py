from pyrogram import Client, filters
from Mangandi import ImageUploader
import requests 


@Client.on_message(filters.command(["upscale", "enhance"]))
async def upscale(bot, m):
    if not message.reply_to_message.photo:
        await message.reply_text("<b>Reply to a Photo</b>")
        return
 
    if message.reply_to_message.photo:
         download = await message.reply_to_message.download()
         media = ImageUploader(k)
         photo = media.upload()
         response = requests.get(f"https://horridapi2-0.onrender.com/upscale?api_key={api_key}&url={photo}&scale=")
         
    
