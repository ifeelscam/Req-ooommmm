#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import Config 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Bot Owner : <a href='tg://user?id={Config.OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Base Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n○ Channel : <a href='https://t.me/ps_updates'>𝙏𝙃𝙀 𝙋𝙎 𝘽𝙊𝙏𝙎</a>\n○ Support Group : <a href='https://t.me/ps_discuss'>𝙋𝙎 - 𝘿𝙄𝙎𝘾𝙐𝙎𝙎𝙄𝙊𝙉 𝙂𝙍𝙊𝙐𝙋</a></b>",
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
