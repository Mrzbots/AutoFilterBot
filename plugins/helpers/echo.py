# credits @XBOTSUPPORTS

from pyrogram import Client, filters, enums
from pyrogram.types import *

@Client.on_message(filters.command("echo"))
async def echo(client, message):
    try:
        # Check user permissions
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        if user.status not in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
            await message.reply_text("You don't have permission to use this command.")
            return
    except Exception as error:
        # Handle case where bot lacks permissions to get member info
        await message.reply_text(f"An error occurred. I may not have permission to check user status. {error}")
        return

    reply = message.reply_to_message
    chat_id = message.chat.id

    if not reply:
        # No message replied to
        await message.reply_text("Please reply to a message to echo its content.")
        return

    await reply.reply_text(message.text.split(None, 1)[1])
    await message.delete()
