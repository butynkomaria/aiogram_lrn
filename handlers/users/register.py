from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import filters

from filters import PHONE_REGEXP
from filters import IsPrivate
from keyboards.default import kb_menu

from loader import dp

from states import register

@dp.message_handler(IsPrivate(), Command('register')) # /register
async def register_(message: types.Message):
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


    await message.answer('Привет, ты начал регистрацию, \nВведи свое имя', reply_markup=name)
    await register.test1.set()

@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state:FSMContext):
    answer = message.text

    await state.update_data(text1=answer)
    await message.answer(f'{answer}, сколько тебе лет?')
    await register.test2.set()

@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state:FSMContext):
    answer = message.text

    await state.update_data(text2=answer)
    data = await state.get_data()
    name = data.get('text1')
    #years = data.get('text2')
    await message.answer(f'{name}, напиши номер своего телефона?')
    await register.test3.set()

@dp.message_handler(filters.Regexp(PHONE_REGEXP), state=register.test3)
async def state4(message: types.Message, state:FSMContext):
    answer = message.text

    print('даа')
    await state.update_data(text3=answer)
    data = await state.get_data()
    name = data.get('text1')
    print(name)
    years = data.get('text2')
    phone =  data.get('text3')
    print(data)
    await message.answer('Регистрация успешно завершена\n'
                         f'Твое имя {name}\n'
                         f'Тебе {years} лет\n'
                         f'Твой номер телефона {phone}', reply_markup=kb_menu)
    await state.finish()


@dp.message_handler(state=register.test3)
async def state3(message: types.Message, state:FSMContext):
    answer = message.text

    await state.update_data(text3=answer)
    data = await state.get_data()
    name = data.get('text1')
    print(name)
    years = data.get('text2')
    phone =  data.get('text3')
    print(data)
    await message.answer('Это не похоже на телефон 😬, попробуем еще раз?', reply_markup=kb_menu)
    await register.test3.set()