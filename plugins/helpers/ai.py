# credits @Mrz_bots

import requests
from HorridAPI import api 
from pyrogram import Client, filters

@Client.on_message(filters.command(["llama", "llamaai", "ask"]))
async def handle_llama_command(client, message):    
    if len(message.command) < 2:
        return await message.reply_text("Please provide query!")
    
    query = " ".join(message.command[1:])
    thinking_message = await message.reply_text("<b>wait...😎</b")

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
        
@Client.on_message(filters.command("ai"))
async def ai(client, message):
    if len(message.text.split(" ", 1)) == 1:
        return await message.reply_text("Provide a query")
        
    prompt = "assistant"
    thinking = await message.reply_text("Thinking ✍️...")
    url = "https://horrid-api.onrender.com/ai"
    headers = {"Content-Type": "application/json"}
    query = message.text.split(" ", 1)[1]  # Get the query from the message    
    data = {"query": query, "prompt": prompt}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        return await message.reply_text(f"Error: {e}")

    try:
        response_json = response.json()        
        await thinking.edit(response_json['response'])
    except (KeyError, TypeError):
        await message.reply_text("Invalid response from the API")
