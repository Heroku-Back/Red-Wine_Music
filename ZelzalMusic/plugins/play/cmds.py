#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, emoji 
from pyrogram import filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZelzalMusic import app



@app.on_message(command(["ميوزك", "الميوزك", "/cmd"]))
async def zdatsr(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/6270c9db2449eab390115.jpg",
        caption=f"""**» مرحبـاً**  {message.from_user.mention} .\n**- استخـدم الازرار بالاسفـل لـ تصفـح اوامـر الميـوزك 🥁**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر التشغيــل •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر القنــاة •", callback_data="zzzch"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر الادمــن •", callback_data="zzzad"),
                ],
            ]
        ),
    )



