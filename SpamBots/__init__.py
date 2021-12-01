from telethon import TelegramClient
from decouple import config
import logging
import time
from os import getenv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
BOT_TOKEN11 = config("BOT_TOKEN11", default=None)
BOT_TOKEN12 = config("BOT_TOKEN12", default=None)
BOT_TOKEN13 = config("BOT_TOKEN13", default=None)
BOT_TOKEN14 = config("BOT_TOKEN14", default=None)
BOT_TOKEN15 = config("BOT_TOKEN15", default=None)
BOT_TOKEN16 = config("BOT_TOKEN16", default=None)
BOT_TOKEN17 = config("BOT_TOKEN17", default=None)
BOT_TOKEN18 = config("BOT_TOKEN18", default=None)
BOT_TOKEN19 = config("BOT_TOKEN19", default=None)
BOT_TOKEN20 = config("BOT_TOKEN20", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

UstaD = TelegramClient('UstaD', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 

UstaD2 = TelegramClient('UstaD2', APP_ID, API_HASH).start(bot_token=BOT_TOKEN2) 

UstaD3 = TelegramClient('UstaD3', APP_ID, API_HASH).start(bot_token=BOT_TOKEN3) 

UstaD4 = TelegramClient('UstaD4', APP_ID, API_HASH).start(bot_token=BOT_TOKEN4) 

UstaD5 = TelegramClient('UstaD5', APP_ID, API_HASH).start(bot_token=BOT_TOKEN5) 

UstaD6 = TelegramClient('UstaD6', APP_ID, API_HASH).start(bot_token=BOT_TOKEN6) 

UstaD7 = TelegramClient('UstaD7', APP_ID, API_HASH).start(bot_token=BOT_TOKEN7) 

UstaD8 = TelegramClient('UstaD8', APP_ID, API_HASH).start(bot_token=BOT_TOKEN8) 

UstaD9 = TelegramClient('UstaD9', APP_ID, API_HASH).start(bot_token=BOT_TOKEN9) 

UstaD10 = TelegramClient('UstaD10', APP_ID, API_HASH).start(bot_token=BOT_TOKEN10)

UstaD11 = TelegramClient('UstaD11', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 

UstaD12 = TelegramClient('UstaD12', APP_ID, API_HASH).start(bot_token=BOT_TOKEN2) 

UstaD13 = TelegramClient('UstaD13', APP_ID, API_HASH).start(bot_token=BOT_TOKEN3) 

UstaD14 = TelegramClient('UstaD14', APP_ID, API_HASH).start(bot_token=BOT_TOKEN4) 

UstaD15 = TelegramClient('UstaD15', APP_ID, API_HASH).start(bot_token=BOT_TOKEN5) 

UstaD16 = TelegramClient('UstaD16', APP_ID, API_HASH).start(bot_token=BOT_TOKEN6) 

UstaD17 = TelegramClient('UstaD17', APP_ID, API_HASH).start(bot_token=BOT_TOKEN7) 

UstaD18 = TelegramClient('UstaD18', APP_ID, API_HASH).start(bot_token=BOT_TOKEN8) 

UstaD19 = TelegramClient('UstaD19', APP_ID, API_HASH).start(bot_token=BOT_TOKEN9) 

UstaD20 = TelegramClient('UstaD20', APP_ID, API_HASH).start(bot_token=BOT_TOKEN10) 
