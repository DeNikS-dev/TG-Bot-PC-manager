import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config:
    URL = os.environ.get("BROWSER_URL")
    TOKEN = os.environ.get("BOT_KEY")
    ADMIN_ID = int(os.environ.get("ADMIN_ID"))

config = Config()

if not config.TOKEN:
    print("---=-=-=-=-=ОТСУТСТВУЕТ ТГ ТОКЕН!!!=-=-=-=-=---")
