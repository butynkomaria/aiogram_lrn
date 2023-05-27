from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import filters
import phonenumbers

from filters import PHONE_REGEXP
from keyboards.default import kb_menu
from utils.db_api import quick_commands as commands
from utils.misc import rate_limit

from loader import dp

from states import register

@dp.message_handler(Command('verify')) # /register
async def register_(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет, {user.first_name}\n'
                                 f'Ты уже настроил получение кодов кодтверждение mos.ru в телеграм')
        elif user.status == 'banned':
            await message.answer(f'Привет {user.first_name}\n'
                                 f'Ты уже забанен')
    except Exception:
        from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

    # подсказка пользователю с его именем из first_name, заполненного в телеграм
        name = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=f'{message.from_user.first_name}')
                ],
            ],
            resize_keyboard=True
        )


        await message.answer('Привет, чтобы получать коды потверждения mos.ru в телеграм введи свое имя.\n'
                             'Подробнее о том, зачем это нужно - /info', reply_markup=name)
        await register.test2.set()



@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state:FSMContext):
    answer = message.text

    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

    # подсказка пользователю - кнопка "поделиться контактом "
    mobnumber = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Поделиться контактом", request_contact=True)
            ],
        ],
        resize_keyboard=True
    )

    await state.update_data(text2=answer)
    data = await state.get_data()
    name = data.get('text2')
    await message.answer(f'{name}, напиши номер своего телефона?', reply_markup=mobnumber)
    await register.test3.set()

# отлавливаем телефон который ввели через кнопку Поделиться контактом
@dp.message_handler(state=register.test3, content_types=types.ContentType.CONTACT)
# отлавливаем телефон который ввели ручками
@dp.message_handler(filters.Regexp(PHONE_REGEXP), state=register.test3)
async def state4(message: types.Message, state:FSMContext):
    if message.text is None:
        answer = message.contact.phone_number
    else:
        answer = message.text

    # форматируем полученный от пользовател телефон в формат +79999999999
    my_number = phonenumbers.parse(answer, "RU")
    answer = phonenumbers.format_number(my_number, phonenumbers.PhoneNumberFormat.E164)

    await state.update_data(text3=answer)
    data = await state.get_data()
    name = data.get('text2')
    mobile =  data.get('text3')


    await commands.add_user(user_id=message.from_user.id,
                                first_name=name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                mobile=mobile,
                                status='active')
    await message.answer('Успех! Теперь ты можешь получать коды подтверждения mos.ru в телеграм.')
    await state.finish()



# обработчик на случай, когда введен НЕ телефон или пользователь передумал регистрироваться
@dp.message_handler(state=register.test3)
async def state3(message: types.Message, state:FSMContext):
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
    # подсказка пользователю - кнопка "поделиться контактом "
    mobnumber = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Поделиться контактом", request_contact=True)
            ],
        ],
        resize_keyboard=True
    )
    answer = message.text

    if answer not in ('Отмена', 'отмена'):
        await state.update_data(text3=answer)
        data = await state.get_data()
        name = data.get('text1')
        print(name)
        years = data.get('text2')
        mobile =  data.get('text3')
        print(data)
        await message.answer('Это не похоже на телефон 😬, попробуем еще раз?\n'
                             'Если передумал регистрирвоаться - введи Отмена', reply_markup=mobnumber)
        await register.test3.set()
    else:
        await message.answer('Регистрация  отменена\n', reply_markup=kb_menu)
        await state.finish()



@rate_limit(limit=3)
@dp.message_handler(text='/profile')
async def get_profile(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user is None:
            await message.answer(f'Ты еще не зарегистрирован\n'
                                 f'Пройти регистрацию - /register')
    except Exception:
        user = await commands.select_user(message.from_user.id)
        await message.answer(f'ID - {user.user_id}\n'
                             f'first_name - {user.first_name}\n'
                             f'last_name - {user.last_name}\n'
                             f'username - {user.username}\n'
                             f'status - {user.status}\n'
                             f'телефон = {user.mobile}'
                             )

