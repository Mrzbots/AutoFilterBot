from pyrogram import Client, filters
import requests

@Client.on_message(filters.command("lyrics"))
async def lyrics(client, message):
    args = message.text.split(" ")
    if len(args) < 2:
        await message.reply_text("Please provide a song name! 🔎")
        return

    song_name = " ".join(args[1:])  
    api = f"https://horrid-api.onrender.com/lyrics?song={song_name}"
    
    try:
        response = requests.get(api)
        response.raise_for_status()  
        data = response.json()
        title = data.get('title', 'Title not found')
        artist = data.get('artist', 'Artist not found')
        lyrics = data.get('lyrics', 'Lyrics not found')

        await message.reply_text(f"Title: {title}\nArtist: {artist}\n\nLyrics:\n{lyrics}")

    except requests.RequestException as e:        
        await message.reply_text(f"Error fetching lyrics: {str(e)}")
    except ValueError:
        await message.reply_text("Error decoding response.")
