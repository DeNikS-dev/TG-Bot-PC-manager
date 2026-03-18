from aiogram.filters import BaseFilter
from aiogram.types import Message
from config import config

class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        user_id = message.from_user.id
        
        return user_id == config.ADMIN_ID
