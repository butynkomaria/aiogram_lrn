from aiogram.types import ContentType, Message, InputFile

from loader import dp

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)

# хендлер отправляет фото, а не file_id фото
@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.from_user.id

    # ИД фото, полученный из предыдущего хендлера
    photo_file_id = 'AgACAgIAAxkBAAIJbGReS2GN5OnyNcHaWQUha8zAhducAAKFyDEb-FDwSr-5vNC6Kr4pAQADAgADeQADLwQ'
    photo_url = ''
    # путь к фото
    photo_bytes = InputFile(path_or_bytesio='media/p.jpg')

    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes)
    #await dp.bot.send_video(chat_id=chat_id, video='BAACAgIAAxkBAAIJemRf1frIaYbWhr1mTxHALhV99u31AAI9KgAC-FAAAUvw-HTAsuho3i8E')


