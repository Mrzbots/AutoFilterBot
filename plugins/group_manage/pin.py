from pyrogram.types import *
from pyrogram import *

@Client.on_message(filters.command("unpin") & filters.group)
async def unpin(client, message: Message):
    reply = message.reply_to_message_id
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    bot_stats = await client.get_chat_member(message.chat.id, "self")
    if not bot_stats.privileges:
        return await message.reply("Iam not Admin 😞")
    elif bot_stats.privileges.can_unpin_chat_message:
        return await message.reply("Sorry dude I don't have pin rights 🙃")
    elif user.privileges.can_unpin_chat_message:
        return await message.reply("you are admin this chat but you don't have pin rights")
    elif not user.privileges:
        return await message.reply("Sorry dude you dont have permission ")
    await client.unpin_chat_message(message.chat.id, reply)    



        
@Client.on_message(filters.command("pin") & filters.group)
async def pin(client, message: Message):
    reply = message.reply_to_message_id
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    bot_stats = await client.get_chat_member(message.chat.id, "self")
    if not bot_stats.privileges:
        return await message.reply("Iam not Admin 😞")
    elif bot_stats.privileges.can_pin_messages:
        return await message.reply("Sorry dude I don't have pin rights 🙃")
    elif user.privileges.can_pin_messages:
        return await message.reply("you are admin this chat but you don't have pin rights")
    elif not user.privileges:
        return await message.reply("Sorry dude you dont have permission ")
    await client.pin_chat_message(message.chat.id, reply)
    
        
