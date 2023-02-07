
class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.used_words = []

    def __repr__(self):
        return f'Игрок по имени {self.user_name}'

    def append_correct_user_word_in_used_words(self, user_word, comp_words):
        '''
        Добавляет введенное слово пользователем в список
        использованных слов, если оно верно.
        '''

        if user_word in comp_words:
            self.used_words.append(user_word)
        return self.used_words

    def get_quantity_user_words(self):
        '''
        Возвращает количество правильно
        составленных игроком слов.
        '''

        return len(self.used_words)

    def was_word_used(self, user_word):
        '''
        Проверяет использовалось ли ранее
        введенное слово игроком. Возвращает
        True или False.
        '''

        return user_word in self.used_words







