#(©)Codexbotz
# Thanks @ps_updates for adding request to sub

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import LOGGER, Config


name ="""
░█████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
██║░░╚═╝██║░░██║██║░░██║█████╗░░░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝
"""


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=Config.API_HASH,
            api_id=Config.APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=Config.TG_BOT_WORKERS,
            bot_token=Config.BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        self.link_one = None
        self.link_two = None
        if Config.CHANNEL_ONE:
            try:
                link_e = (await self.create_chat_invite_link(chat_id=Config.CHANNEL_ONE, creates_join_request=True)).invite_link 
                self.link_one = link_e                                     
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the CHANNEL_ONE value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {CHANNEL_ONE}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                sys.exit()
        if Config.CHANNEL_TWO:
            try:
                link_f = (await self.create_chat_invite_link(chat_id=Config.CHANNEL_TWO, creates_join_request=True)).invite_link 
                self.link_two = link_f                                  
            except Exception as b:
                self.LOGGER(__name__).warning(b)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the CHANNEL_TWO value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {Config.CHANNEL_TWO}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
                sys.exit()
        try:
            db_channel = await self.get_chat(Config.CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/CodeXBotzSupport for support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/CodeXBotz")
        self.LOGGER(__name__).info(f""" \n\n       
░█████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
██║░░╚═╝██║░░██║██║░░██║█████╗░░░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
██║░░██╗██║░░██║██║░░██║██╔══╝░░░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝
                                          """)
        self.username = usr_bot_me.username
        # web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
