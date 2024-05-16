from pyrogram.types import *
from pyrogram import *

@Client.on_message(filters.command("unpin_all") & filters.group)
async def unpinall(client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    bot_stats = await client.get_chat_member(message.chat.id, "self")
    if not bot_stats.privileges:
        return await message.reply("Iam not Admin 😞")
    elif bot_stats.status.can_unpin_all_chat_messages and not message.reply_to_message:
        return await message.reply("Sorry dude I don't have pin rights 🙃")
    elif user.status.can_unpin_all_chat_messages and not message.reply_to_message:
        return await message.reply("you are admin this chat but you don't have pin rights")
    elif not user.privileges:
        return await message.reply("Sorry dude you dont have permission ")
    await client.unpin_all_chat_messages(message.chat.id)    



        
@Client.on_message(filters.command("pin") & filters.group)
async def pin_handler(client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    bot_stats = await client.get_chat_member(message.chat.id, "self")
    if not bot_stats.privileges:
        return await message.reply("Iam not Admin 😞")
    elif bot_stats.status.can_pin_messages and not message.reply_to_message:
        return await message.reply("Sorry dude I don't have pin rights 🙃")
    elif user.status.can_pin_messages and not message.reply_to_message:
        return await message.reply("you are admin this chat but you don't have pin rights")
    elif not user.privileges:
        return await message.reply("Sorry dude you dont have permission ")
    await client.pin_chat_message(message.chat.id, msg)
    
        
