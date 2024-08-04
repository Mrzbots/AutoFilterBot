# credits @Mrz_bots

import requests
from HorridAPI import api 
from pyrogram import Client, filters

@lient.on_message(filters.command("ask"))
async def ask(client, message):    
    if len(message.command) < 2:
        return await message.reply_text("Please provide query!")
    
    query = " ".join(message.command[1:])
    thinking_message = await message.reply_text("<b>wait...😎</b>")
    try:        
        response = api.llama(query)        
        await thinking_message.edit(f"Hey, {message.from_user.mention}!\nQuery: {query}\nResult:\n{response}")

    except Exception as e:        
        error_message = f"Hmm, something went wrong: {str(e)}"[:100] + "...\n use /bug comment"
        await thinking_message.edit(error_message)
        
