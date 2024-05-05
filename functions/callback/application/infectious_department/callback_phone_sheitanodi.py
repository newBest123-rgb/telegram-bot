from aiogram import types

from text.text_application.text_phone_sheitanidi import \
    TEXT_PHONE

from keyboards.inlain_keyboards.keyboards_back.inlain_back_and_menu import kb_back
from config.api_token import PARSE_MODE_HTML


async def callback_phone(callback: types.CallbackQuery):
    if callback.data == 'leave_phone_number':
        await callback.message.answer(text=TEXT_PHONE,
                                      reply_markup=kb_back,
                                      parse_mode=PARSE_MODE_HTML)
