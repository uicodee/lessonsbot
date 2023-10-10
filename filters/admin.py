from aiogram.filters import BaseFilter
from aiogram.types import Message

from data.data import ADMIN_ID, blocklist, admins


class AdminFilter(BaseFilter):
    def __init__(self, admin_id: int):
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> bool:
        # return message.from_user.id not in blocklist
        return message.from_user.id in admins
        # return message.from_user.id == ADMIN_ID
