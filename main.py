import requests
from basicWord import BasicWord
from player import Player
from utils import load_random_word


if __name__ == '__main__':

    DATA_SOURCE = requests.get('https://www.jsonkeeper.com/b/7BW7')

    if DATA_SOURCE.status_code == 200:

        user_name = input('Введите имя игрока ')
        player = Player(user_name)

        print(f'Привет, {player.user_name.title()}')

        basicWord = load_random_word(DATA_SOURCE, BasicWord)

        print(f'Составьте {basicWord.quantity_word()} слов из слова {basicWord.word}')
        print('Слова должны быть не короче 3 букв')
        print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
        print('Поехали, ваше первое слово?')

        while len(player.used_words) < basicWord.quantity_word():

            user_word = input('')

            if user_word.lower() == 'stop' or user_word == 'стоп':
                break
            elif len(user_word) < 3:
                print('Сликом короткое слово')
            elif user_word not in basicWord.subWords:
                print('Неверно')
            elif user_word in player.used_words:
                print('Уже использовано')
            else:
                player.append_correct_user_word_in_used_words(user_word, basicWord.subWords)
                print('Верно')

        print(f'Игра завершена, вы угадали {player.get_quantity_user_words()} слов')

    else:
        print('Ошибка загрузки данных с сервера, попробуйте позже')





