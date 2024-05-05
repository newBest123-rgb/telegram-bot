from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ib1 = InlineKeyboardButton(text='Дрепа Т.Г.',
                           callback_data='__drepa_doctors__')

ib2 = InlineKeyboardButton(text='Куданетов К.А.',
                           callback_data='__kudanetov_doctors__')

ib3 = InlineKeyboardButton(text='Карханина В.А.',
                           callback_data='__karkhanina_doctors__')

ib4 = InlineKeyboardButton(text='Пашина А.Ю.',
                           callback_data='__pashina_doctors__')

ib5 = InlineKeyboardButton(text='Суханова А.С.',
                           callback_data='__sukhanova_doctors__')

ib6 = InlineKeyboardButton(text='Погорелова Д.А.',
                           callback_data='__pogorelova_doctors__')

ib_menu = InlineKeyboardButton(text='⬆️Вернуться в меню',
                               callback_data='back_menu')

ib_back = InlineKeyboardButton(text='⬅️Назад',
                               callback_data='back')

kb_name_doctors = InlineKeyboardMarkup()

kb_name_doctors.add(ib1, ib2, ib3)
kb_name_doctors.add(ib4, ib5)
kb_name_doctors.add(ib6)
kb_name_doctors.add(ib_menu)
kb_name_doctors.add(ib_back)
