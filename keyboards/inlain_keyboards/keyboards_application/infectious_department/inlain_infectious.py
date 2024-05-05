from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ib1 = InlineKeyboardButton(text='👨🏻‍⚕️Показать врачей',
                           callback_data='show_doctors_infectious_department')

ib2 = InlineKeyboardButton(text='📝Записаться',
                           callback_data='sign_up_infectious_department')

ib_menu = InlineKeyboardButton(text='⬆️Вернуться в меню',
                               callback_data='back_menu')

ib = InlineKeyboardButton(text='⬅️Назад',
                          callback_data='back')

inline_infectious = InlineKeyboardMarkup()

inline_infectious.add(ib1, ib2)
inline_infectious.add(ib_menu)
inline_infectious.add(ib)
