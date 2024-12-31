#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={Config.OWNER_ID}'>ᴅᴀᴛᴛᴇʙᴀʏᴏ</a>\n○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ  : <a href='https://t.me/+S6jna9Xe3-UyODhl'>ᴢɪᴘ ғɪʟᴇ </a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴅᴇᴠʟᴏᴘᴇʀ ', url='https://t.me/Outlawbots')
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
