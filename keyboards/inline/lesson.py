from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_datas.callback_datas import Lesson
from data.data import lessons


def lessons_keyboard(category_id: int) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for lesson in lessons.get(category_id):
        builder.button(
            text=lesson.get('name'),
            callback_data=Lesson(id=lesson.get('id'))
        )
    builder.button(
        text="Ortga",
        callback_data="back"
    )
    builder.adjust(1)
    return builder.as_markup()
