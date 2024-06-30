
from pyrogram import Client, filters
from info import ADMINS
from subprocess import getoutput as run
import asyncio
import os
import io

@Client.on_message(filters.command(["sh", "shell"]) & filters.user(ADMINS))
async def shell(client, message):    
    if len(message.command) < 2:
        await message.reply("Give an input!")
        return
    code = message.text.split(None, 1)[1]
    message_text = await message.reply_text("`Running`")
    output = run(code)
    if len(output) > 4096:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "shell.txt"
            await message.reply_document(
                document=out_file, disable_notification=True
            )
            await message_text.delete()
    else:
        await message_text.edit(f"Output:\n{output}")
