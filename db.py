import aiosqlite
from config.config import DB_PATH

async def init_db():
    """Создает таблицу для хранения сообщений, если её нет."""
    async with aiosqlite.connect(DB_PATH) as db:
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
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO messages (message_id, chat_id, user_id, text, date)
            VALUES (?, ?, ?, ?, ?)
        """, (message_id, chat_id, user_id, text, date))
        await db.commit()

async def get_messages_after_last_recorded(chat_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        # Найдём последнее сообщение с "СПИСАНО"
        cursor = await db.execute(
            "SELECT message_id FROM messages WHERE chat_id = ? AND text LIKE '%СПИСАНО%' ORDER BY message_id DESC LIMIT 1",
            (chat_id,)
        )
        last_record = await cursor.fetchone()

        if not last_record:
            return []  # Если "СПИСАНО" не найдено, возвращаем пустой список

        last_message_id = last_record[0]

        # Получаем все сообщения после него
        cursor = await db.execute(
            "SELECT text FROM messages WHERE chat_id = ? AND message_id > ? ORDER BY message_id",
            (chat_id, last_message_id)
        )
        messages = await cursor.fetchall()

        return [msg[0] for msg in messages]
