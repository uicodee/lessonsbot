from aiogram import Router, types, F
from aiogram.filters import CommandStart

from keyboards.inline.category import category_keyboard

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message) -> None:
    await message.answer(
        text=f"Assalomu alaykum, {message.from_user.full_name}\n"
             f"Kerakli kategoriyani tanlang",
        reply_markup=category_keyboard()
    )


@router.message(F.video)
async def on_video(message: types.Message) -> None:
    await message.answer(text=message.video.file_id)
