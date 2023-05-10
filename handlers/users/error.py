from aiogram import types
from loader import dp

@dp.message_handler()
async def comand_erroe(message: types.Message):
    await message.answer(f'команда:  {message.text} не найдена')