from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ib2 = InlineKeyboardButton(text='⬆️Вернуться в меню',
                           callback_data='back_menu')

ib_back = InlineKeyboardButton(text='⬅️Назад',
                               callback_data='back')

kb_back = InlineKeyboardMarkup()

kb_back.add(ib2)
kb_back.add(ib_back)
