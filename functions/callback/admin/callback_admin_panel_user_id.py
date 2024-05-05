from aiogram import types


async def callback_admin_users_id(callback: types.CallbackQuery):
    if callback.data == 'show_users':
        pass
