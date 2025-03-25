import aiosqlite

DB_NAME = "bot_database.db"  # Имя файла базы данных

async def init_db():
    """Создает таблицу для хранения сообщений, если её нет."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id INTEGER NOT NULL,
                chat_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                text TEXT,
                date TEXT NOT NULL
            )
        """)
        await db.commit()

async def save_message(message_id: int, chat_id: int, user_id: int, text: str, date: str):
    """Сохраняет сообщение в базу данных."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT INTO messages (message_id, chat_id, user_id, text, date)
            VALUES (?, ?, ?, ?, ?)
        """, (message_id, chat_id, user_id, text, date))
        await db.commit()
