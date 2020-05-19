import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time


if bool(os.environ.get("WEBHOOK", False)):
    from file_resource import Resources
else:
    from resources import Resources

from shorts import Shorts

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from supports.chatbaseclass import BujukkuChatBase
from supports.process_status import ui_display_process
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image


@pyrogram.Client.on_message(pyrogram.Filters.command(["customname"]))
async def rename_doc(robot, changer):
    if changer.from_user.id not in Resources.REGISTERED_ACCOUNTS:
        await robot.delete_messages(
            chat_id=changer.chat.id,
            message_ids=changer.message_id,
            revoke=True
        )
        return
    BujukkuChatBase(changer.from_user.id, changer.text, "customname")
    if (" " in changer.text) and (changer.reply_to_message is not None):
        cmd, fname = changer.text.split(" ", 1)
        if len(fname) > 100:
            await changer.reply_text(
                Shorts.FNAME_BIG.format(
                    fnamelimit="100",
                    num=len(fname)
                )
            )
            return
        description = Shorts.USER_CAPTION_FILE_TEXT
        file_dl_location = Resources.FILE_DL_LOCATION + "/"
        a = await robot.send_message(
            chat_id=changer.chat.id,
            text=Shorts.INITIATE_DOWNLOAD,
            reply_to_message_id=changer.message_id
        )
        c_time = time.time()
        original_file_dl_location = await robot.download_media(
            message=changer.reply_to_message,
            fname=file_dl_location,
            progress=ui_display_process,
            progress_args=(
                Shorts.INITIATE_DOWNLOAD,
                a,
                c_time
            )
        )
        if original_file_dl_location is not None:
            try:
                await robot.edit_message_text(
                    text=Shorts.SUCCESS_DOCUMENT_DOWNLOAD,
                    chat_id=changer.chat.id,
                    message_id=a.message_id
                )
            except:
                pass
            # if "IndianMovie" in the_real_download_location:
            #     await bot.edit_message_text(
            #         text=Shorts.ERROR_403_RENAME,
            #         chat_id=changer.chat.id,
            #         message_id=a.message_id
            #     )
            #     return

            fname_new = file_dl_location + fname
            os.rename(original_file_dl_location, fname_new)

            logger.info(original_file_dl_location)
            thumb_image_path = Resources.file_dl_location + "/" + str(changer.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                thumb_image_path = None
            else:
                width = 0
                height = 0
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                img.resize((320, height))
                img.save(thumb_image_path, "JPEG")
            c_time = time.time()
            await robot.send_document(
                chat_id=changer.chat.id,
                document=fname_new,
                thumb=thumb_image_path,
                caption=description,
                reply_to_message_id=changer.reply_to_message.message_id,
                progress=ui_display_process,
                progress_args=(
                    Shorts.INITIATE_UPLOAD,
                    a,
                    c_time
                )
            )
            try:
                os.remove(fname_new)
                os.remove(thumb_image_path)
            except:
                pass
            await robot.edit_message_text(
                text=Shorts.FILE_UPLOAD_DONE_TEXT,
                chat_id=changer.chat.id,
                message_id=a.message_id,
                disable_web_page_preview=True
            )
    else:
        await robot.send_message(
            chat_id=changer.chat.id,
            text=Shorts.CHANGE_FILE_NAME_ACK,
            reply_to_message_id=changer.message_id
        )
