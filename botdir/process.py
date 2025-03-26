def process_messages(messages: list[str]):
    # Твоя логика анализа сообщений
    word_count = sum(len(msg.split()) for msg in messages)  # Просто считаем слова
    return f"Общее количество слов: {word_count}"
