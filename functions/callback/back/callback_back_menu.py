from aiogram import types

from text.text_commands_bot.text_command_start import START_TEXT
from keyboards.inlain_keyboards.keyboards_menu.inlain_menu import ikb
from config.api_token import PARSE_MODE_HTML


async def callback_back_menu_query_questions(callback: types.CallbackQuery):
    if callback.data == 'back_menu':
        await callback.message.answer(text=START_TEXT,
                                      reply_markup=ikb,
                                      parse_mode=PARSE_MODE_HTML)
