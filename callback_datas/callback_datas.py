from aiogram.filters.callback_data import CallbackData


class LessonsCategory(CallbackData, prefix="category"):
    id: int


class Lesson(CallbackData, prefix="lesson"):
    id: int
