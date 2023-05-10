from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default import kb_test
from keyboards.inline import ikb_menu, ikb_menu2
from loader import dp

@dp.message_handler(text='Инлайн меню')
async def show_inline_menu(message: types.Message):
    await message.answer('Инлайн кнопки ниже', reply_markup=ikb_menu) # напишет в чат 'Инлайн кнопки ниже'


#реакция на кажатие на inline-кнопки
@dp.callback_query_handler(text='Сообщение')
async def send_message(call: CallbackQuery):
    await call.message.answer('Кнопки заменены', reply_markup=kb_test)


@dp.callback_query_handler(text='alert')
async def send_message(call: CallbackQuery):
    await call.answer('Кнопки заменены') # отобразит во всплывающем окне на пару сек фразу 'Инлайн кнопки ниже'
    # await call.answer('Кнопки заменены', show_alert=True) # отобразит в поп-ап  фразу 'Инлайн кнопки ниже' который явно нужно будет закрыть



@dp.callback_query_handler(text='Кнопки2')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ikb_menu2)