from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ib1 = InlineKeyboardButton(text='Шейтаниди Л.Л.',
                           callback_data='__sheitanidi_doctors__')

ib2 = InlineKeyboardButton(text='Шевцова Н.П.',
                           callback_data='__shevtsova_doctors__')

ib3 = InlineKeyboardButton(text='Федулова А.А.',
                           callback_data='__fedulova_doctors__')

ib4 = InlineKeyboardButton(text='Кривоногова Н.Н.',
                           callback_data='__krivonogova_doctors__')

ib5 = InlineKeyboardButton(text='Воронкина Е.Н.',
                           callback_data='__voronkina_doctors__')

ib_menu = InlineKeyboardButton(text='⬆️Вернуться в меню',
                               callback_data='back_menu')

ib_back = InlineKeyboardButton(text='⬅️Назад',
                               callback_data='back')

kb_name_doctors = InlineKeyboardMarkup()

kb_name_doctors.add(ib1, ib2, ib3)
kb_name_doctors.add(ib4, ib5)
kb_name_doctors.add(ib_menu)
kb_name_doctors.add(ib_back)
