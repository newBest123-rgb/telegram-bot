from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_application.text_cardiology_departament.text_cardiology_application_doctors import \
    CARDIOLOGY_DOCTORS_APLICATION_TEXT

from keyboards.inlain_keyboards.keyboards_application.cardiology_department.inlain_cardiology import inline_cardiology


async def callback_query_main_cardiology(callback: types.CallbackQuery):
    if callback.data == 'cardiology_department':
        await callback.message.answer(text=CARDIOLOGY_DOCTORS_APLICATION_TEXT,
                                      parse_mode=PARSE_MODE_HTML,
                                      reply_markup=inline_cardiology)
