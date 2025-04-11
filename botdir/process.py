# TODO
# 1) first stage - milk processing
#   1.1) detect product name inside message, if there is any
#   1.2) detect volume
#   1.3) detect category
#   1.4) sum it up by product and category
# 2) create ultra dictionary or db for naming
# 3) make this dic not hardcoded, easy to manage from outside

# for now it's ok, but in future make it NOT hardcoded, so you can add new keys not througn code,
# but from outside
# DON'T FORGET TO LOWER STRING BEFORE COMPARING TO SYNONYMS
from botdir.dictionaries import names, categories


def reverse_dic(dic):
    synonym_to_main = {} # reverse dic used to search synonyms
    for main_name, synonym_list in dic.items():
       for synonym in synonym_list:
            synonym_to_main[synonym] = main_name
    return synonym_to_main


names = reverse_dic(names)
categories = reverse_dic(categories)


def process_messages(messages: list[str]):
    # Твоя логика анализа сообщений
    # word_count = sum(len(msg.split()) for msg in messages)  # Просто считаем слова
    total = {}
    for message in messages:

        # change it later how to handle when you have multiple products in one message
        split_message = message.split(' ')
        if len(split_message) != 3:
            continue
        product_name, product_amount, category = split_message

        # normalizing name
        product_name = product_name.lower()
        normalized_name = names.get(product_name, product_name)

        # normalizing categories
        category = category.lower()
        normalized_category = categories.get(category, category)

        # search
        key = (normalized_name, normalized_category) # tuple like (мк, порча)
        if key in total: # check if key already exists
            total[key] += int(product_amount) # maybe later change to float, bc some shi is float
        else:
            total[key] = int(product_amount) # check this moment, mb i don't have to check
                                            # whether key exists or nah
    #return f"Общее количество слов: {word_count}"
    return total
