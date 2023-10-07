from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.inline.category import category_keyboard
from keyboards.inline.lesson import lessons_keyboard

router = Router()


@router.callback_query(F.data == "back_main")
async def back_to_main(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(
        text=f"Assalomu alaykum, {callback.from_user.full_name}\n"
             f"Kerakli kategoriyani tanlang",
        reply_markup=category_keyboard()
    )


@router.callback_query(F.data == "back_category")
async def back_to_category(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    category_id = int(data.get('category_id'))
    await callback.message.delete()
    await callback.message.answer(
        text="Kerakli darsni tanlang",
        reply_markup=lessons_keyboard(category_id=category_id)
    )
