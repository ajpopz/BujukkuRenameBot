import os

class Resources(object):
    CB_TOKEN = os.environ.get("CB_TOKEN", "")
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    REGISTERED_ACCOUNTS = set(int(x) for x in os.environ.get("REGISTERED_ACCOUNTS", "").split())
    # AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    # the download location, where the HTTP Server runs
    FILE_DL_LOCATION = "./DOWNLOADS"
    # SAVE_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 1572864000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 1572864000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://i.postimg.cc/5t0KVhnN/photo-2020-05-05-18-50-00.jpg")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""