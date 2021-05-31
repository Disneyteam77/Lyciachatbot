from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
Hello, I am [Erza](https://telegra.ph/file/fd5626da803978cd8f8c9.mp4), an AI Powered ChatBot. If You Are Feeling Lonely, You can Always Come to me and Chat With Me!
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("🦋 CЯΣΛƬӨЯ 🦋", url = "https://t.me/Yeageristbotsdev"), InlineKeyboardButton("🦋UPDATATES 🦋", url = "https://t.me/Animemusicarchive6")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
