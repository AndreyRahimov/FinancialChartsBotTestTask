from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.company_names import get_company_names


class IsCompanyName(BaseFilter):
    async def __call__(self, message: Message, database) -> bool:
        return message.text in get_company_names(database)
