async def on_startup(dp):
    import filters
    filters.setup(dp)
    import middlewares

    middlewares.setup(dp)

    from loader import db
    from utils.db_api.db_gino import on_startup
    print('Подключение к PostgreSQL')
    await on_startup(dp)

    #print('Удаление БД')
    #await db.gino.drop_all()

    print('Создание таблиц')
    await db.gino.create_all()
    print('Готово')

    from utils.notify_admins import on_startup_notify # оповещаем администраторов о том, что бот старотовал
    await on_startup_notify(dp)


    from utils.set_bot_comands import set_default_comands
    await set_default_comands(dp)

    print('Бот запущен')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)