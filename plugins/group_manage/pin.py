from pyrogram.types import *
from pyrogram import *

@Client.on_message(filters.command("unpin_all") & filters.group)
async def unpinall(client, message:Message):
    try:
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        bot_stats = await client.get_chat_member(message.chat.id, "self")
        if not bot_stats.status.can_change_info:
            return await message.reply("Iam not Admin 😞")
        elif bot_stats.status.can_pin_messages and not message.reply_to_message:
            return await message.reply("Sorry dude I don't have pin rights 🙃")
        elif user.status.can_pin_messages and not message.reply_to_message:
            return await message.reply("you are admin this chat but you don't have pin rights")
        elif not user.status:
            return await message.reply("Sorry dude you dont have permission ")
        await client.unpin_all_chat_messages(message.chat.id)
    except Exception as e:
        await message.reply_text(f"{e}")

@Client.on_message(filters.command("pin") & filters.group)
async def pin_handler(client, message:Message):
    try:
        msg = message.reply_to_message.message_id
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        if user.status not in [types.ChatMemberStatus.OWNER, types.ChatMemberStatus.ADMINISTRATOR]:
            raise PermissionError("You are not allowed to use this command")
        await client.pin_chat_message(message.chat.id, msg)
    except Exception as e:
        await message.reply_text(f"{e}")
