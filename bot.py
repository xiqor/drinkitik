import asyncio
from aiogram import Bot, Dispatcher
from config.config import BOT_TOKEN
from botdir.handlers import router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(router)

    print("🚀 Бот запущен!")
    await dp.start_polling(bot)  # Новый способ запуска в aiogram 3

if __name__ == "__main__":
    asyncio.run(main())  # Запускаем асинхронный event loop
