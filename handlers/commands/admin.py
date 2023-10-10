from aiogram import Router, types
from aiogram.filters import Command

from data.data import ADMIN_ID
from filters.admin import AdminFilter

router = Router()


@router.message(
    AdminFilter(admin_id=ADMIN_ID),
    Command(commands=["admin"])
)
async def on_cmd_admin(message: types.Message) -> None:
    await message.answer(
        text="Welcome"
    )

# Don't Repeat Yourself
