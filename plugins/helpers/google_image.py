import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto


@Client.on_message(filters.command(["image", "img"]))
async def pinterest(client, message):
    chat_id = message.chat.id

    try:
        query = message.text.split(maxsplit=1)[1]  # Get query string after command
    except IndexError:
        return await message.reply("Please provide an image name to search for.")

    url = f"https://pinterest-api-one.vercel.app/?q={query}"  # Construct the API URL

    # Make the request using requests library (remove 'get' from imports)
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    try:
        images_data = response.json()
        images = images_data["images"][:6]  # Limit to 6 images
    except (KeyError, json.JSONDecodeError):
        return await message.reply("Error fetching images from Pinterest.")

    media_group = []
    for image_url in images:
        media_group.append(InputMediaPhoto(media=image_url))

    # Send media group instead of editing the message repeatedly
    await message.reply("`Serching...`")
    try:
        await client.send_media_group(
            chat_id=chat_id, media=media_group, reply_to_message_id=message.id
        )
    except Exception as e:
        await message.reply(f"Error: {e}")
