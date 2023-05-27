from aiogram import types


async def set_default_comands(dp):
    await dp.bot.set_my_commands([
        #types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('verify', 'Верификация в боте')
    ])