# TODO
# 1) first stage - milk processing
#   1.1) detect product name inside message, if there is any
#   1.2) detect volume
#   1.3) detect category
#   1.4) sum it up by product and category
# 2) create ultra dictionary or db for naming

# for now it's ok, but in future make it NOT hardcoded, so you can add new keys not througn code,
# but from outside
# DON'T FORGET TO LOWER STRING BEFORE COMPARING TO SYNONYMS
naming = {
    'Мбн': ['мбн',
            'молоко банан', 'банан молоко',
            'молоко банановое', 'банановое молоко',
            'молоко бн', 'бн молоко',
            'м банан', 'банан м',
            'м банановое', "банановое м"],
    'Мбз': ['мбз', 'безлактоза', 'безлактоза',
            'молоко безлактоза', 'безлактоза молоко',
            'молоко безлактозное', 'безлактозное молоко',
            'молоко бз', 'бз молоко',
            'м безлактоза', 'безлактоза м',
            'м безлактозное', "безлактозное м"],
    'Мкк': ['мкк',
            'молоко кокос', 'кокос молоко',
            'молоко кокосовое', 'кокосовое молоко',
            'молоко кк', 'кк молоко',
            'м кокос', 'кокос м',
            'м кокосовое', 'кокосовое м'],
    'Мк': ['мк', 'корова',
           'молоко корова', 'корова молоко',
           'молоко коровье', 'коровье молоко',
           'молоко к', 'к молоко',
           'м коровье', 'коровье м',
           'м корова', 'корова м'],
    'Ммд': ['ммд', 'миндаль', 'миндальное',
           'молоко миндаль', 'миндаль молоко',
           'молоко миндальное', 'миндальное молоко',
           'молоко мд', 'мд молоко',
           'м миндаль', 'миндаль м',
           'м миндальное', 'миндальное м'],
    'Мо': ['мо', 'овсяное',
           'молоко овсянка', 'овсянка молоко',
           'молоко овсяное', 'овсяное молоко',
           'молоко о', 'о молоко',
           'м овсяное', 'овсяное м',
           'м овсянка', 'овсянка м'],
}

synonym_to_main = {} # reverse dic used to search synonyms
for main_name, synonym_list in naming.items():
        for synonym in synonym_list:
            synonym_to_main[synonym] = main_name

def process_messages(messages: list[str]):
    # Твоя логика анализа сообщений
    # word_count = sum(len(msg.split()) for msg in messages)  # Просто считаем слова
    total = {}
    for message in messages:

        # change it later how to handle when product is more than two words
        split_message = message.split(' ')
        if len(split_message) != 3:
            continue
        product_name, product_amount, category = split_message

        # normalizing name
        product_name = product_name.lower()
        normalized_name = synonym_to_main.get(product_name, product_name)

        # search
        key = (normalized_name, category) # tuple like (мк, порча)
        if key in total: # check if key already exists
            total[key] += int(product_amount) # maybe later change to float, bc some shi is float
        else:
            total[key] = int(product_amount) # check this moment, mb i don't have to check
                                            # whether key exists or nah
    #return f"Общее количество слов: {word_count}"
    return total
