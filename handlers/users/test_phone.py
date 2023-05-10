from aiogram import types
from loader import dp
from aiogram.dispatcher import filters

from filters import PHONE_REGEXP
from utils.misc import rate_limit

@rate_limit(limit=15)

@dp.message_handler(filters.Regexp(PHONE_REGEXP))
async def regexp_example(msg: types.Message):
    await msg.answer('Похоже на номер телефона, не так ли?')