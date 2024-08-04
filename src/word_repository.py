import random
from typing import List


class WordRepository:
    def __init__(self, file: List[str]):
        self.__file = file
        self.__list_words = [line.strip() for line in self.__file]

    def get_random_word(self) -> str:
        return random.choice(self.__list_words)
