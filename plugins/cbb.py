#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 👑 Creator : <a href='tg://user?id={OWNER_ID}'>RG</a>\n○ ⚜ Anime in Hindi: <a href='https://t.me/Dub_Anime_in_Hindi'>Join</a>\n○ ⚜ Anime Series: <a href='https://t.me/Anime_Series_in_Hindi_Dubbed'>Join</a>\n○ ⚜ Anime Movies: <a href='https://t.me/Dub_Anime_Movies_in_Hindi'>Join</a>\n○ ⚜ Hindi Official: <a href='https://t.me/Crunchyroll_Anime_Hindi_Official'>Join</a>\n○ ⚜ Any Problem: @RG_Anime_Group</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
