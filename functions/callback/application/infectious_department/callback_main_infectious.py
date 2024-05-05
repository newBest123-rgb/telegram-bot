from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_application.text_infections_departament.text_infectious_application_doctors import \
    INFECTIOUS_DOCTORS_APLICATION_TEXT

from keyboards.inlain_keyboards.keyboards_application.infectious_department.inlain_infectious import inline_infectious


async def callback_query_main_infectious(callback: types.CallbackQuery):
    if callback.data == 'infectious_department':
        await callback.message.answer(text=INFECTIOUS_DOCTORS_APLICATION_TEXT,
                                      parse_mode=PARSE_MODE_HTML,
                                      reply_markup=inline_infectious)
