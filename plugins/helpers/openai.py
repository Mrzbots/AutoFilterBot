# credits @Mrz_bots

import requests
from HorridAPI.AiGenerativeContent import AiGenerativeContent
from pyrogram import Client, filters

generate_content = AiGenerativeContent.gen_content

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
        response = await generate_content(payload, 5)
        content = response['response']
        await mes.edit(f"Hey {message.from_user.mention},\n\nQuery: {query}\n\nResult:\n\n{content}")

    except Exception as e:  
        # print(e)
        error_message = f"Hmm, something went wrong: {str(e)}"[:100] + "...\n use /bug comment"
        await mes.edit(error_message)
