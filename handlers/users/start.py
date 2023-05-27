from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("start"))
async def menu(message: types.Message):
    await message.answer("Через бота можно получать коды подтверждения для входа на портал mos.ru.\n"
                         "\n"
                         "Для получения подробной информации выбери /info.\n"
                         "Для верификации в боте - /verify.")
