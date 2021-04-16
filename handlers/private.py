from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CRXGZ2AACAQRgeSaH5kaX_BeOtmSJDNe5ov1eTAACpQADPjM0M7Zwa5Abkh7CHgQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [OVIN](https://t.me/oViNc).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📩 Contact Me 📩", url="https://t.me/oViNc")
                ],[
                    InlineKeyboardButton(
                        "🌀 Powered", url="https://t.me/MultiAkunProduct"
                    ),     
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/NollepAlliance"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Namexian"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/OurMusicplaybot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Namexian")
                ]
            ]
        )
   )


