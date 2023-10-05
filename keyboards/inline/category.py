from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_datas.callback_datas import LessonsCategory
from data.data import lessons_categories


def category_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for category in lessons_categories:
        builder.button(
            text=category.get('name'),
            callback_data=LessonsCategory(id=category.get('id'))
        )
    builder.adjust(1)
    return builder.as_markup()
