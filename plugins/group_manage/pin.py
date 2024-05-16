from pyrogram import *
from pyrogram.types import *


@Client.on_message(filters.command("unpin_all") & filters.group)
async def unpinall(client, message: Message):
    try:
     user = await client.get_chat_member(message.chat.id , message.from_user.id)
     bot_stats = await bot.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await message.reply("Iam not Admin 😞")
     elif bot_stats.privileges.can_unpin_all_chat_messages and not message.reply_to_message:
         return await message.reply("Sorry dude I don't have pin rights 🙃")
     elif user.privileges.can_unpin_all_chat_messages and not message.reply_to_message:
         return await message.reply("you are admin this chat but you don't have pin rights")
     elif not user.privileges:
         return await message.reply("Sorry dude you dont have permission ")
    await client.unpin_all_chat_messages(message.chat.id)
    except Exception as e:
     await message.reply_text(f"{e}")


@Client.on_message(filters.command("pin") & filters.group)
async def pin_handler(client: user, message: Message):
    try:
     msg = message.reply_to_message_id
     user = await client.get_chat_member(message.chat.id , message.from_user.id)
     if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
         raise PermissionError("You are not allowed to use this command")
     await client.pin_chat_message(message.chat.id, msg)
    except Exception as e:
     await message.reply_text(f"{e}")
      

      
