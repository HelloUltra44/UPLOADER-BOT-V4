import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("6177960676:AAFLbeajZKzsf3wkDtrMkfn7v6sv57S3C0s", "")

    API_ID = int(os.environ.get("API_ID", 12998595))

    API_HASH = os.environ.get("API_HASH", "1f2749a6cf463db8910e62be793923cb")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "877460799").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @UploadLinkToFileBot"

    DATABASE_URL = os.environ.get("mongodb+srv://Pknk198:$198%Faisal@pknk198.hqzb2kh.mongodb.net/?retryWrites=true&w=majority", "")

    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001642382009))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "877460799"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "https://t.me/+e9zc_xULQhpkZWQ1")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Faisalhasan_bot")

    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))

    PRO_USERS.append(OWNER_ID)
