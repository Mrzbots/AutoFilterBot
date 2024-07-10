# credits @Mrz_bots

import requests
from pyrogram import Client, filters

# Define a descriptive constant for the API URL
API_URL = "https://horrid-api.onrender.com/llama"

@Client.on_message(filters.command(["llama", "llamaai", "ask"]))
async def handle_llama_command(client, message):
    """Processes user queries using the Llama AI API."""

    # Check for missing input with a clear and concise message
    if len(message.command) < 2:
        return await message.reply_text("Hey!   Please provide some text for me to analyze.")

    # Extract the user's query and provide initial feedback
    query = " ".join(message.command[1:])
    thinking_message = await message.reply_text(" Thinking like a llama...")

    try:
        # Fetch response from Llama AI using f-string formatting
        response = requests.get(f"{API_URL}?query={query}").json()

        # Craft a well-formatted response message
        response_message = f"""
Hey, {message.from_user.mention}! 

Query: {query}

Result:
{response['response']}
"""

        # Edit the thinking message to display the result
        await thinking_message.edit(response_message)

    except Exception as e:
        # Handle errors gracefully with a user-friendly message
        error_message = f"Hmm, something went wrong: {str(e)}"[:100] + "..."
        await thinking_message.edit(error_message)

@Client.on_message(filters.command("palm"))
async def palm(client, message):
    if len(message.text.split(" ", 1)) == 1:
        return await message.reply_text("Provide a query")
    
    query = message.text.split(" ", 1)[1]
    
    api = f"https://horrid-api.onrender.com/palm?query={query}"
    response = requests.get(api)
    result = response.json().get("result", "No result found")
    
    s = await message.reply_text("Thinking 💭")
    await s.edit(result)


@Client.on_message(filters.command("ai"))
async def ai(client, message):
    prompt = "assistant"
    url = "https://horrid-api.onrender.com/ai"
    headers = {"Content-Type": "application/json"}
    query = message.text.split(" ", 1)[1]  # Get the query from the message

    if not query:
        return await message.reply_text("Please provide a query with /ai")

    data = {"query": query, "prompt": prompt}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        return await message.reply_text(f"Error: {e}")

    try:
        response_json = response.json()
        thinking = await message.reply_text("Thinking ✍️...")
        await thinking.edit(response_json['response'])
    except (KeyError, TypeError):
        await message.reply_text("Invalid response from the API")
