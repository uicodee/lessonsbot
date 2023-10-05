from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from callback_datas.callback_datas import LessonsCategory
from keyboards.inline.lesson import lessons_keyboard

router = Router()


@router.callback_query(LessonsCategory.filter())
async def on_lesson_category(callback: types.CallbackQuery, callback_data: LessonsCategory, state: FSMContext) -> None:
    print("Lesson category ID:", callback_data.id)
    await callback.message.edit_text(
        text="Kerakli darsni tanlang",
        reply_markup=lessons_keyboard(category_id=callback_data.id)
    )
    await state.update_data(category_id=callback_data.id)
