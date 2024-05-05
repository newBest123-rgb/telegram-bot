from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ib1 = InlineKeyboardButton(text='Инфекционное отделение',
                           callback_data='infectious_department')

ib2 = InlineKeyboardButton(text='Хирургическое отделение',
                           callback_data='surgical_department')

ib3 = InlineKeyboardButton(text='Отделение кардиологии',
                           callback_data='cardiology_department')

ib4 = InlineKeyboardButton(text='Рентгеновское отделение',
                           callback_data='x_ray_department')

ib5 = InlineKeyboardButton(text='Травматолого-ортопедическое отделение',
                           callback_data='traumatology_orthopaedic_department')

ib = InlineKeyboardButton(text='⬅️Назад',
                          callback_data='back')

inline_main_application = InlineKeyboardMarkup()

inline_main_application.add(ib1, ib2, ib3)
inline_main_application.add(ib4, ib5)

inline_main_application.add(ib)
