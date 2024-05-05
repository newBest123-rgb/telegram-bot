from aiogram import types

from text.text_application.text_cardiology_departament.text_show_cardiology_doctors import TEXT_SHOW_DOCTORS
from keyboards.inlain_keyboards.keyboards_application.cardiology_department.inlain_back_menu_cardiology import kb_back
from config.api_token import PARSE_MODE_HTML


async def callback_show_doctors_cardiology(callback: types.CallbackQuery):
    if callback.data == 'show_doctors_cardiology_department':
        await callback.message.answer(text=TEXT_SHOW_DOCTORS,
                                      reply_markup=kb_back,
                                      parse_mode=PARSE_MODE_HTML)
