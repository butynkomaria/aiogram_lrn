from aiogram import types
from loader import dp


from filters import IsPrivate
from utils.misc import rate_limit

@rate_limit(limit=15)
@dp.message_handler(IsPrivate(), text='/start')
async def comand_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}! \n'
                         f'Твой айди:  {message.from_user.id}')