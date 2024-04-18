from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from bot import Bot
from config import Config
from database.database import db

@Bot.on_chat_join_request(filters.chat(Config.CHANNEL_ONE) | filters.chat(Config.CHANNEL_TWO))
async def join_reqs(client, join_req: ChatJoinRequest):
    user_id = join_req.from_user.id
    if join_req.chat.id == Config.CHANNEL_ONE:
        try:
            await db.add_req_one(user_id)
        except Exception as e:
            print(f"Error adding join request to req_one: {e}")
    elif join_req.chat.id == Config.CHANNEL_TWO:
        try:
            await db.add_req_two(user_id)
        except Exception as e:
            print(f"Error adding join request to req_two: {e}")
