from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

PHONE_REGEXP = r'^(\+?)([78]?) ?\(?([9]{1})([0-9]{2})\)? ?([0-9]{3})[- ]?([0-9]{2})[- ]?([0-9]{2})$'

