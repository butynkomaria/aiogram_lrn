from aiogram import Bot
from data import config
from aiogram.types import Message

bot = Bot(config.BOT_TOKEN)


async def ss(chat_id, msg: str):
    try:
        await bot.send_message(chat_id, msg)
        return 200
    except:
        await bot.send_message(chat_id, msg)
        return 500