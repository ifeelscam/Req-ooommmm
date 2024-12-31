import os
import logging
from logging.handlers import RotatingFileHandler

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7045740764:AAFBZXStfn-CZGAQstxxY5_iBhUFsC5DHwA")
    APP_ID = int(os.environ.get("APP_ID", "24371796"))
    API_HASH = os.environ.get("API_HASH", "8121c78f4b8b31e88cc2623d1277338d")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002016717904")) # db Channel id 
    CHANNEL_ONE = int(os.environ.get("CHANNEL_ONE", "-1002431157485")) #request to sub Channel id
    CHANNEL_TWO = int(os.environ.get("CHANNEL_TWO", "-1002403716155")) #request to sub Channel id
    OWNER_ID = int(os.environ.get("OWNER_ID", "1439890119"))
    PORT = os.environ.get("PORT", "8080")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Outlawbots:Zoro@cluster0.huekk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Hitokiri_Battousai_Bot")
    FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
    TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
    START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\nɪ ᴀᴍ ᴍᴜʟᴛɪ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ , ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
    try:
      ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "5696112220 7162615398 6076683960").split()]
    except ValueError:
      raise Exception("Your Admins list does not contain valid integers.")
    ADMINS.append(OWNER_ID)
    FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 𝐒𝐢𝐫/𝐌𝐚𝐦 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬..\n\n𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧....!</b>")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
    PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
    DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True' else False
    BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
    USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @DATTEBAYO56"
    LOG_FILE_NAME = "filexsharerobbot.txt"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            Config.LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
