from aiogram.filters import BaseFilter
from aiogram.types import Message


class UsernameFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.username is not None
