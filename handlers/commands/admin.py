from aiogram import Router, types
from aiogram.filters import Command

from data.data import ADMIN_ID, users
from filters.admin import AdminFilter
from filters.username import UsernameFilter

router = Router()


@router.message(
    AdminFilter(admin_id=ADMIN_ID),
    UsernameFilter(),
    Command(commands=["admin"])
)
async def on_cmd_admin(message: types.Message) -> None:
    txt = ""
    for user in users:
        txt += f"{user.get('name')}\n"
    await message.answer(
        text=txt
    )

# Don't Repeat Yourself (DRY)
