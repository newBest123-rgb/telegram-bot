from aiogram import types

from text.text_application.text_infections_departament.text_show_infectious_doctors import TEXT_SHOW_DOCTORS
from keyboards.inlain_keyboards.keyboards_application.infectious_department.inlain_back_menu_infectious import kb_back
from config.api_token import PARSE_MODE_HTML


async def callback_show_doctors_infectious(callback: types.CallbackQuery):
    if callback.data == 'show_doctors_infectious_department':
        await callback.message.answer(text=TEXT_SHOW_DOCTORS,
                                      reply_markup=kb_back,
                                      parse_mode=PARSE_MODE_HTML)
