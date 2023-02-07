import random


def load_random_word(data_source, ClassName):
    data_json = data_source.json()
    random_index = data_json[random.randint(0, len(data_json) - 1)]
    random_word = random_index["word"]
    random_subwords = random_index["subwords"]
    class_instance = ClassName(random_word, random_subwords)
    return class_instance






