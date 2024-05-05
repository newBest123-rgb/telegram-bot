from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_application.text_application import APLICATION_TEXT

from keyboards.inlain_keyboards.keyboards_application.inlain_main_application import inline_main_application


async def callback_query_aplication(callback: types.CallbackQuery):
    if callback.data == 'application':
        await callback.message.answer(text=APLICATION_TEXT,
                                      parse_mode=PARSE_MODE_HTML,
                                      reply_markup=inline_main_application)
