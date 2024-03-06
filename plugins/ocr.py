# (c) Koshik Kumar (@KoshikKumar17)

import os
from PIL import Image
import pytesseract # pip install pytesseract (requirements.txt)
from pyrogram import Client as Koshik
from pyrogram import filters


@Koshik.on_message(filters.command(["ocr"]))
async def ocr_command(bot, message):
    z = await message.reply_text("__Checking...⚡__", quote=True)
    preimg = message.reply_to_message
    if preimg:
        if preimg.file_size < 10 * 1024 * 1024:
            img = await bot.download_media(preimg)
            txt = pytesseract.image_to_string(Image.open(img))
            if txt:
                await message.reply_text(txt, quote=True)
            else:
                await message.reply_text("**Failed to perform OCR on the provided image.**", quote=True)
            os.remove(img)
        else:
            await z.edit_text("**Send image less than 10 MB**")
    else:
        await z.edit_text("**Please reply to any image**")
