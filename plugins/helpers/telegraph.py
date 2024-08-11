from pyrogram import Client, filters
from telegraph import upload_file
import os

@Client.on_message(filters.command('telegraph'))
async def telegraph(client, message):
    if message.reply_to_message:
        if message.reply_to_message.photo or message.reply_to_message.video:
            msg = await message.reply_text("Uploading to Telegraph...")
            reply = message.reply_to_message
            if message.reply_to_message.photo:
                file = await reply.download()
                file_name = file
            else:
                file = await reply.download()
                file_name = file
            response = upload_file((file_name, open(file, 'rb')))
            await msg.edit(f"Telegraph Link: `https://telegra.ph{response[0]}`")
            os.remove(file)
        else:
            await message.reply_text("Please reply to a photo or video.")
    else:
        await message.reply_text("Please reply to a message containing a photo or video.")
