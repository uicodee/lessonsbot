from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def back_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Ortga",
        callback_data="back"
    )
    return builder.as_markup()
