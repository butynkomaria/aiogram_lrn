from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("info"))
async def menu(message: types.Message):
    await message.answer("Через бота можно получать коды подтверждения для входа на портал mos.ru - для прохождении двухфакторной аутентификации или восстановлении пароля.\n"
                         "\n"
                         "Это может быть удобно в случае, когда получение кодов в СМС или на электнонную почту невозможно.\n"
                         "Рекомендум пройти верификацию в боте, выбрав пункт меню /verify, чтобы настроить этот метод получения кодов подтвреждения в телеграм.")
