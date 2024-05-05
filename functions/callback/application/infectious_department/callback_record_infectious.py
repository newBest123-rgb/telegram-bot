from aiogram import types

from text.text_application.text_choice_doctors import TEXT_CHOICE_DOCTORS
from keyboards.inlain_keyboards.keyboards_application.infectious_department.inlain_name_doctors_infectious import kb_name_doctors
from config.api_token import PARSE_MODE_HTML


async def callback_sign_up_infectious(callback: types.CallbackQuery):
    if callback.data == 'sign_up_infectious_department':
        await callback.message.answer(text=TEXT_CHOICE_DOCTORS,
                                      reply_markup=kb_name_doctors,
                                      parse_mode=PARSE_MODE_HTML)
