from aiogram import Router
from aiogram.types import Message
from db import save_message

messages_router = Router()

@messages_router.message()
async def log_message(message: Message):
    """Логирует все сообщения в БД"""
    await save_message(
        message_id=message.message_id,
        chat_id=message.chat.id,
        user_id=message.from_user.id,
        text=message.text or "",
        date=message.date.isoformat()
    )
