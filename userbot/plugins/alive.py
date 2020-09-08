# For @TeleBotHelp
"""Check if your userbot is working."""
import asyncio
import requests
from PIL import Image
from io import BytesIO
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet, check pinned in @TeleBotHelp"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    
   
        await borg.send_message(alive.chat_id, f"**Welcome To SBot **\n\n"
            "**`Hey! I'm alive. All systems online and functioning normally!`**\n\n"
            "` ✦ Telethon version:` **1.15.0**\n` 🔹 Python:` **3.8.3**\n"
            "` ✦ More info:` [TeleBot](https://telegra.ph/TeleBot-07-08)\n"
            "` ✦ Bot created by:` [LEOALEX](https://t.me/leoalextg)\n"
            "` ✦ Database Status:` **All OK 👌!**\n"
            f"` ✦ My pro owner`: {DEFAULTUSER}\n\n"
            "    [✨ GitHub Repository ✨](https://github.com/xditya/TeleBot)", link_preview = False)
        await borg.send_file(alive.chat_id, file=sticker) 
        await alive.delete()
