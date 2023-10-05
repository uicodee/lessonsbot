from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from callback_datas.callback_datas import Lesson
from data.data import lessons

router = Router()


@router.callback_query(Lesson.filter())
async def on_lesson(callback: types.CallbackQuery, callback_data: Lesson, state: FSMContext) -> None:
    print("Lesson ID:", callback_data.id)
    data = await state.get_data()
    category_id = int(data.get('category_id'))
    await callback.message.delete()
    for lesson in lessons.get(category_id):
        if lesson.get('id') == callback_data.id:
            await callback.message.answer_video(
                video=lesson.get('file_id'),
                caption=lesson.get('name')
            )

