from aiogram import types
from loader import dp

@dp.message_handler(text='/hello')
async def comand_hello(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
