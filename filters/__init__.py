from aiogram import Dispatcher

from .phone_number import PHONE_REGEXP


def setup(dp: Dispatcher):
    dp.filters_factory.bind(PHONE_REGEXP)