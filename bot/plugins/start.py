from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hi {m.from_user.mention}, \n\nI'm Sample Video Generator Bot Made By @ViralBeatz. I can also provide screenshot & Sample from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel ", url="https://t.me/ViralBeatz"
                    ),
                    InlineKeyboardButton("Movies Channel", url="https://t.me/ViralBeatz"),
                ],
                [InlineKeyboardButton("My Father", url="https://t.me/ViralBeatz")],
            ]
        ),
    )
