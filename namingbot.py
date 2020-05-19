import logging
logging.basicResources(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

if bool(os.environ.get("WEBHOOK", False)):
    from file_resources import Resources
else:
    from resources import Resources

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    if not os.path.isdir(Resources.FILE_DL_LOCATION):
        os.makedirs(Resources.FILE_DL_LOCATION)
    addons = dict(
        root="addons"
    )
    app = pyrogram.Client(
        "BujukkuRenamerBot",
        bot_token=Resources.TELEGRAM_BOT_TOKEN,
        api_id=Resources.APP_ID,
        api_hash=Resources.API_HASH,
        plugins=addons
    )
    app.set_parse_mode("html")
    Resources.REGISTERED_ACCOUNTS.add(1048115250)
    app.run()