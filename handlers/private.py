from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CSt8d2QACAUlgf_NYWhflczsb3FrmohwFdKP5JQACBwMAAuaPAAFU6ygyxboYvPUeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [𝐃𝐇𝐀𝐑𝐌𝐀](https://t.me/Devilsangry) Source by [oViNc](https://t.me/oViNc)

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📩 Contact Me 📩", url="https://t.me/ourmusicbots")
                ],[
                    InlineKeyboardButton(
                        "🌀 Powered", url="https://t.me/oViNc"
                    ),     
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/testingsongs"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/dontfuckingshit"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/transsongbot?startgroup=true"
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
                        "🔊 Channel", url="https://t.me/dontfuckingshit")
                ]
            ]
        )
   )


