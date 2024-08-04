from typing import Dict, List


def print_info_board(dict_info_game: Dict[str, List[str]], cnt_attempts: int) -> None:
    for key, value in dict_info_game.items():
        print(f'{key}({len(value)} букв): ', *value)
    print(f'Количество попыток: {cnt_attempts}\n')


def show_menu() -> None:
    print('Меню')
    items = ['Новая игра', 'Выход']

    print('=' * (len(max(items)) + 3))

    for i, item in enumerate(items):
        print(f'{i + 1}. {item}')

    print('=' * (len(max(items)) + 3))


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
