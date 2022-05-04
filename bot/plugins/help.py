from pyrogram import filters

from bot.screenshotbot import ScreenShotBot
from bot.config import Config


HELP_TEXT = """
Hi {mention}. Welcome to Converter Bot Made By @ViralBeatz. 
You can use me to generate:

    1. Screenshots.
    2. Sample Video.
    3. Trim Video.

Send A Video Select Which You Need To Do By Me. Wait A Few Seconds. 

Send /settings For More Info & Choose Which Need. 


__If issues persists contact @ViralBeatz.__

{admin_notification}
"""
ADMIN_NOTIFICATION_TEXT = (
    "Since you are one of the admins, you can check /admin to view the admin commands."
)


@ScreenShotBot.on_message(filters.private & filters.command("help"))
async def help_(c, m):

    await m.reply_text(
        text=HELP_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        quote=True,
    )
