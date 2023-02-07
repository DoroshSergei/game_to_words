
class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subWords = subwords

    def __repr__(self):
        return f'Игровое слово - {self.word}'

    def is_correct(self, user_word):
        '''
        Проверяет есть ли введенное игроком
        слово в перечне слов, которые можно составить
        из игрового слова. Возвращает True или False.
        '''

        return user_word in self.subWords

    def quantity_word(self):
        '''
        Возвращает максимальное количество слов,
        которое можно составить из игрового слова.
        '''

        return len(self.subWords)













