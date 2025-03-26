from aiogram import Router, types
from aiogram.filters import Command
from config.config import ALLOWED_CHATS
from db import get_messages_after_last_recorded
from botdir.process import process_messages

handlers_router = Router()  # Используем Router вместо Dispatcher

@handlers_router.message(Command("parse"))
async def parse_messages(message: types.Message):
    chat_id = message.chat.id
    messages = await get_messages_after_last_recorded(chat_id)

    if chat_id not in ALLOWED_CHATS:
        await message.answer("❌ Этот чат не в списке разрешенных!")
        return

    if not messages:
        await message.answer("❌ Не найдено сообщений после последнего 'СПИСАНО'.")
        return

    print("✅ Хендлер /parse вызван!")  # Отладка
    await message.answer("Парсинг начался...")
    # Тут ты добавишь свою логику обработки сообщений
    result = process_messages(messages)

    await message.answer(f"✅ Обработано {len(messages)} сообщений.\nРезультат: {result}")
