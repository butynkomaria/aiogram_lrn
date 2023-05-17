from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.db_api.db_gino import db

from data import config

# Создаем переменную бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# Создаем зранилище в оперативной памяти
storage = MemoryStorage()

# Создаем диспетчер
dp = Dispatcher(bot,storage=storage)

__all__ =['bot', 'storage', 'dp', 'db']

