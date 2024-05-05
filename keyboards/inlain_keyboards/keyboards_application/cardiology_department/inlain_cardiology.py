from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ib1 = InlineKeyboardButton(text='👨🏻‍⚕️Показать врачей',
                           callback_data='show_doctors_cardiology_department')

ib2 = InlineKeyboardButton(text='📝Записаться',
                           callback_data='sign_up_cardiology_department')

ib_menu = InlineKeyboardButton(text='⬆️Вернуться в меню',
                               callback_data='back_menu')

ib = InlineKeyboardButton(text='⬅️Назад',
                          callback_data='back')

inline_cardiology = InlineKeyboardMarkup()

inline_cardiology.add(ib1, ib2)
inline_cardiology.add(ib_menu)
inline_cardiology.add(ib)
