import os
from urllib.parse import unquote, urlparse
import re
import traceback
import sys
import random
import aiohttp
import requests
import traceback
from lycia import LYCIA
from datetime import datetime
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    CallbackQuery,
    InlineQuery,
    InlineQueryResultAnimation,
)   
from pykeyboard import InlineKeyboard

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
    return data


@LYCIA.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()

    answers = []
    if string.split()[0] == "lycia":
            if len(string.split()) < 2:
                await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text='Erza | Chat [text]',
                    switch_pm_parameter='lycia',
                )
                return
            Erza = string.split(None, 1)[1].strip()
            Erza = await ErzaChat_bot(answers, Erza)
            await client.answer_inline_query(
                query.id,
                results=Erza,
                cache_time=2
            )
   

async def ErzaChat_bot(answers, text):
    URL = f"https://api.affiliateplus.xyz/api/chatbot?message={text}&botname=@ErzaChat_bot&ownername=@Yeageristbotsdev"
    result = await fetch(URL)
    buttons = InlineKeyboard(row_width=1)
    buttons.add(InlineKeyboardButton(
        "Erza",
        switch_inline_query_current_chat="Erza"
    ))
    caption = f"""
**You:** `{text}`
**Erza:** `{result['message']}`"""
    answers.append(
        InlineQueryResultPhoto(
            photo_url="https://telegra.ph/file/c0de581cf0f2123f108df.jpg",
            title="Erza",
            description=result['message'],
            caption=caption,
            reply_markup=buttons
        ))
    return answers
