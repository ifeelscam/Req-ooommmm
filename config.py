import os
import logging
from logging.handlers import RotatingFileHandler

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) # db Channel id 
    CHANNEL_ONE = int(os.environ.get("CHANNEL_ONE", "")) request to sub Channel id
    CHANNEL_TWO = int(os.environ.get("CHANNEL_TWO", "")) request to sub Channel id
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    PORT = os.environ.get("PORT", "8080")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    DATABSE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
    TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
    START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in specified channels, and other users can access them from special links.")
    try:
      ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "1280356202 853554999").split()]
    except ValueError:
      raise Exception("Your Admins list does not contain valid integers.")
    ADMINS.append(OWNER_ID)
    FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel/Group to use me\n\nPlease join the channel.</b>")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
    PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
    DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True' else False
    BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
    USER_REPLY_TEXT = "❌Don't send me messages directly. I'm only a File Share bot!"
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
