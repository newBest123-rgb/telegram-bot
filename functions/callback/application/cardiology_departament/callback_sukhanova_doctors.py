from aiogram import types

from text.text_application.text_cardiology_departament.text_main_sukhanova_doctors import TEXT_SUKHANOVA_DOCTORS

from keyboards.inlain_keyboards.keyboards_application.infectious_department.inlain_back_and_phone import kb_back
from config.api_token import PARSE_MODE_HTML


async def callback_sukhanova_doctors(callback: types.CallbackQuery):
    if callback.data == '__sukhanova_doctors__':
        await callback.message.answer(text=TEXT_SUKHANOVA_DOCTORS,
                                      reply_markup=kb_back,
                                      parse_mode=PARSE_MODE_HTML)
