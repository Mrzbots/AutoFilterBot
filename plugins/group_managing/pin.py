from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import filters, enums 
from pyrogram.types import *


async def admin_check(message: Message) -> bool:
    if not message.from_user:
        return False

    if message.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return False

    if message.from_user.id in [
        777000,  # Telegram Service Notifications
        1087968824  # GroupAnonymousBot
    ]:
        return True

    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    admin_strings = [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]
    # https://git.colinshark.de/PyroBot/PyroBot/src/branch/master/pyrobot/modules/admin.py#L69
    if check_status.status not in admin_strings:
        return False
    else:
        return True

async def admin_filter_f(filt, client, message):
    return await admin_check(message)

admin_fliter = filters.create(func=admin_filter_f, name="AdminFilter")


@Client.on_message(filters.command("pin") & admin_fliter)
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()
    await message.reply_text("I Have Pinned That message")


@Client.on_message(filters.command("unpin") & admin_fliter)             
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
    await message.reply_text("I Have UnPinned That message")


@Client.on_message(filters.command("unpin_all") & filters.group)
async def unpinall_handler(client, message: Message):
    try:
     user = await client.get_chat_member(message.chat.id , message.from_user.id)
     if user.status not in [enums.ChatMemberStatus.OWNER , enums.ChatMemberStatus.ADMINISTRATOR]:
         raise PermissionError("You are not allowed to use this command")
     await client.unpin_all_chat_messages(message.chat.id)
    except Exception as e:
     await message.reply_text(f"{e}")
