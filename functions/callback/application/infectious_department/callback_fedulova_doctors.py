from aiogram import types

from text.text_application.text_infections_departament.text_main_fedulova_doctors import TEXT_FEDULOVA_DOCTORS

from keyboards.inlain_keyboards.keyboards_application.infectious_department.inlain_back_and_phone import kb_back
from config.api_token import PARSE_MODE_HTML


async def callback_fedulova_doctors(callback: types.CallbackQuery):
    if callback.data == '__fedulova_doctors__':
        await callback.message.answer(text=TEXT_FEDULOVA_DOCTORS,
                                      reply_markup=kb_back,
                                      parse_mode=PARSE_MODE_HTML)
