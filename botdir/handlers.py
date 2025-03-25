from aiogram import Router, types
from aiogram.filters import Command
from botdir.parser import parse_chat
from config.config import ALLOWED_CHATS
from db import save_message

router = Router()  # Используем Router вместо Dispatcher

@router.message()
async def log_message(message: types.Message):
    """Логирует все сообщения в БД"""
    await save_message(
        message_id=message.message_id,
        chat_id=message.chat.id,
        user_id=message.from_user.id,
        text=message.text or "",
        date=message.date.isoformat()
    )

@router.message(Command("parse"))
async def parse_chat_command(message: types.Message):
    chat_id = message.chat.id  # Получаем ID чата

    # Проверяем, разрешен ли этот чат
    if chat_id not in ALLOWED_CHATS:
        await message.answer("❌ Этот чат не в списке разрешенных!")
        return

    # Запускаем парсинг
    messages = await parse_chat(chat_id)
    await message.answer(f"✅ Найдено {messages} сообщений после 'УЧТЕНО'.")
