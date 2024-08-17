# credits @Mrz_bots

import requests
from HorridAPI.AiGenerativeContent import AiGenerativeContent
from pyrogram import Client, filters


@Client.on_message(filters.command("openai"))
async def openai(client, message):
    text = " ".join(message.command[1:])
    if len(message.command) < 2:
        return await message.reply_text("Please provide query!")
    if message.reply_to_message:
        query = f"{message.reply_to_message.text} {text}"
    else:
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
        ai = AiGenerativeContent
        response = ai.gen_content(payload, 5)
        content = response['response']
        await mes.edit(f"Hey {message.from_user.mention},\n\nQuery: {query}\n\nResult:\n\n{content}")

    except Exception as e:  
        # print(e)
        error_message = f"Hmm, something went wrong: {str(e)}"[:100] + "...\n use /bug comment"
        await mes.edit(error_message)
