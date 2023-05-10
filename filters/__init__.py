from aiogram import Dispatcher

from .private_chat import IsPrivate
from .phone_number import PHONE_REGEXP


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)

def setup2(dp: Dispatcher):
    dp.filters_factory.bind(PHONE_REGEXP)