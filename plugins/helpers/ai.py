# credits @Mrz_bots

import requests
from HorridAPI import api 
from pyrogram import Client, filters

@Client.on_message(filters.command("ask"))
async def handle_llama_command(client, message):    
    if len(message.command) < 2:
        return await message.reply_text("Please provide query!")
    
    query = " ".join(message.command[1:])
    thinking_message = await message.reply_text("<b>wait...😎</b>")

    try:
        # response 
        response = api.llama(query)

        # Craft a well-formatted response message
        response_message = f"""
Hey, {message.from_user.mention}! 

Query: {query}

Result:
{response}
"""

        # Edit the thinking message to display the result
        await thinking_message.edit(response_message)

    except Exception as e:
        # Handle errors gracefully with a user-friendly message
        error_message = f"Hmm, something went wrong: {str(e)}"[:100] + "..."
        await thinking_message.edit(error_message)
        
