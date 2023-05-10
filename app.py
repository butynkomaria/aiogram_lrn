async def on_startup(dp):

    import filters
    filters.setup(dp)
    import middlewares
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


    from utils.set_bot_comands import set_default_comands
    await set_default_comands(dp)

    print('Бот запущен')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)