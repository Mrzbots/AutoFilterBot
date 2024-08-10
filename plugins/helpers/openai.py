# credits @Mrz_bots

import requests
from HorridAPI.AiGenerativeContent import AiGenerativeContent
from pyrogram import Client, filters

openai = AiGenerativeContent.gen_content

@Client.on_message(filters.command("openai"))
async def openai(client, message):    
    if len(message.command) < 2:
        return await message.reply_text("Please provide query!")
    
    query = " ".join(message.command[1:])
    mes = await message.reply_text("🌚")
    payload = {
        "messages": [                    
            {            
                "role": "user", 
                "content": query
            }
        ]
    }
    try:        
        response = openai(payload, 5)          
        await message.reply_text(f"Hey {message.from_user.mention},\n\nQuery: {query}\n\nResult:\n\n{response}")
        await mes.delete()

    except Exception as e:  
        # print(e)
        error_message = f"Hmm, something went wrong: {str(e)}"[:100] + "...\n use /bug comment"
        await thinking_message.edit(error_message)
