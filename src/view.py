from typing import Dict, List


def print_info_board(dict_info_game: Dict[str, List[str]]) -> None:
    print(f'Загаданное слово({len(dict_info_game["masked_hidden_word"])} букв): ',
          *dict_info_game["masked_hidden_word"])
    print(f'Доступные буквы({len(dict_info_game["available_letters"])} букв): ', *dict_info_game["available_letters"])
    print(f'Использованные буквы({len(dict_info_game["used_letters"])} букв): ', *dict_info_game["used_letters"])
    print(f'Количество попыток: {dict_info_game["cnt_attempts"]}\n')


def show_menu() -> None:
    print('Меню')
    items = ['Новая игра', 'Мои результаты', 'Выход']

    print('=' * (len(max(items, key=len)) + 3))

    for i, item in enumerate(items):
        print(f'{i + 1}. {item}')

    print('=' * (len(max(items, key=len)) + 3))


def show_win_message(hidden_word: str) -> None:
    print('\nПобеда! Угаданы все буквы')
    print(f'Загаданное слово: {hidden_word}\n')


def show_loose_message(hidden_word: str) -> None:
    print('\nПоражение. Все попытки использованы')
    print(f'Загаданное слово: {hidden_word}\n')


def show_incorrect_letter_error() -> None:
    print('\n***Введен неверный символ***\n')


def show_incorrect_command_error() -> None:
    print('\n***Нет данной команды***\n')


def show_game_results(dict_game_results: Dict) -> None:
    print(f'''
        Статистика по играм:
-------------------------------------
|Побед: {dict_game_results['cnt_win']}
|Поражений: {dict_game_results['cnt_loose']}
=====================================
|Среднее количество попыток: {dict_game_results['mean_attempts']}
-------------------------------------\n''')
