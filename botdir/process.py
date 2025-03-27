# TODO
# 1) first stage - milk processing
#   1.1) detect product name inside message, if there is any
#   1.2) detect volume
#   1.3) detect category
#   1.4) sum it up by product and category
# 2) create ultra dictionary or db for naming


def process_messages(messages: list[str]):
    # Твоя логика анализа сообщений
    #word_count = sum(len(msg.split()) for msg in messages)  # Просто считаем слова
    total = {}
    for message in messages:
        split_message = message.split(' ')
        if len(split_message) != 3:
            continue
        product_name, product_amount, category = message.split(' ') # teach him how to handle when product is more than two words
        key = (product_name, category) # tuple like (мк, порча)
        if key in total: # check if key already exists
            total[key] += int(product_amount) # maybe later change to float, bc some shi is float
        else:
            total[key] = int(product_amount) # check this moment, mb i don't have to check whether key exists or nah
    #return f"Общее количество слов: {word_count}"
    return total
