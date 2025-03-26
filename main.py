import asyncio
from aiogram import Bot, Dispatcher
from config.config import BOT_TOKEN
from db import init_db
from botdir.handlers import handlers_router
from botdir.messages import messages_router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(handlers_router)
    dp.include_router(messages_router)

    await init_db()

    print("🚀 Бот запущен!")
    await dp.start_polling(bot)  # Новый способ запуска в aiogram 3

if __name__ == "__main__":
    asyncio.run(main())  # Запускаем асинхронный event loop
