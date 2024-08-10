from typing import Dict, List

from src.hangman_stages import get_hangman_stage


class HangmanGame:
    def __init__(self, hidden_word: str):
        self.__hidden_word = hidden_word
        self.__masked_hidden_word = ['_'] * len(self.__hidden_word)

        self.__available_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.__used_letters = ''

        self.__cnt_attempts = 6
        self.__pointer_stages = -1

    def make_move(self, input_letter) -> None:
        if input_letter not in self.__used_letters:
            if input_letter in self.__hidden_word:
                self.open_hidden_letter(input_letter)
            else:
                print('\n***Данной буквы нет в загаданном слове***')
                self.__cnt_attempts -= 1
                self.__pointer_stages += 1

            self.__available_letters = self.__available_letters.replace(input_letter, '')
            self.__used_letters += input_letter
        else:
            print('\n***Данная буква уже была использована***')

        self.show_hangman_stage()

    def show_hangman_stage(self) -> None:
        if self.__pointer_stages >= 0 and self.check_state_game() in (0, -1):
            print(get_hangman_stage(self.__pointer_stages))

    def open_hidden_letter(self, input_letter: str) -> None:
        for i, letter in enumerate(self.__hidden_word):
            if self.__hidden_word[i] == input_letter:
                self.__masked_hidden_word[i] = input_letter

    def check_state_game(self) -> int:
        if self.__cnt_attempts == 0:
            return -1

        if '_' not in self.__masked_hidden_word:
            return 1

        return 0

    def get_cnt_attempts(self) -> int:
        return self.__cnt_attempts

    def get_hidden_word(self) -> str:
        return self.__hidden_word

    def get_info_game(self) -> Dict[str, List[str]]:
        return {"hidden_word": self.__masked_hidden_word,
                "available_letters": self.__available_letters,
                "used_letters": self.__used_letters,
                "game_result": self.check_state_game(),
                "cnt_attempts": self.__cnt_attempts}

    @staticmethod
    def is_correct_letter(letter: str) -> bool:
        return letter.isalpha() and len(letter) == 1 and letter.lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
