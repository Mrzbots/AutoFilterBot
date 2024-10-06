from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database.bs import bss

def get_pm_search_status():
    user_data = bss.find_one()
    if user_data:
        return user_data.get("pm_search", False)
    return False

def update_pm_search_status(status):
    bss.update_one({}, {"$set": {"pm_search": status}}, upsert=True)

@Client.on_message(filters.command(["bs", "bsettings"]))
async def bs_settings(client, message):
    pm_search_status = get_pm_search_status()
    if pm_search_status:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("PM Search ✔️", callback_data="pm_search_off"),
                ]
            ]
        )
    else:
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("PM Search ❌", callback_data="pm_search_on"),
                ]
            ]
        )
    await message.reply("Bot Settings:", reply_markup=keyboard)

@Client.on_callback_query()
async def callback_query_handler(client, callback_query):
    data = callback_query.data
    if data == "pm_search_on":
        update_pm_search_status(True)
        await callback_query.edit_message_text("PM Search is now ON ✔️")
    elif data == "pm_search_off":
        update_pm_search_status(False)
        await callback_query.edit_message_text("PM Search is now OFF ❌")
