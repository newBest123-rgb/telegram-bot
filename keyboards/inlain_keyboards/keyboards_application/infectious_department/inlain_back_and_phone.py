from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ib1 = InlineKeyboardButton(text='📝Оставить номер телефона',
                           callback_data='leave_phone_number')

ib2 = InlineKeyboardButton(text='⬆️Вернуться в меню',
                           callback_data='back_menu')

ib_back = InlineKeyboardButton(text='⬅️Назад',
                               callback_data='back')

kb_back = InlineKeyboardMarkup()

kb_back.add(ib1)
kb_back.add(ib2)
kb_back.add(ib_back)
