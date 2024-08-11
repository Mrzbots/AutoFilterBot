from pyrogram import Client, filters
import requests

@Client.on_message(filters.command("news"))
async def latest_news(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Please provide query")
    
    query = message.text.split(" ")[1]  
    response = requests.get(f"https://horrid-api.onrender.com/news?query={query}")
    news_data = response.json()
    news_title = news_data.get("title")
    news_source = news_data.get("source")
    news_url = news_data.get("url")
    await client.send_message(chat_id=message.chat.id, text=f"📰 Latest News:\n\nTitle: {news_title}\nSource: {news_source}\nURL: {news_url}")
 
