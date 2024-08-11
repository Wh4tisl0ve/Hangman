import os
from typing import List
from abc import ABC, abstractmethod

import pandas as pd


class Reader(ABC):
    @abstractmethod
    def read_file(self, filename):
        pass


class TxtFileReader(Reader):
    def __init__(self):
        self.__path = 'src/data'

    def read_file(self, filename) -> List[str]:
        try:
            with open(f'{self.__path}/{filename}', 'r', encoding='UTF-8') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f'Не найден файл со словами\n')
            exit()
        except Exception as ex:
            print(f'Произошла ошибка: {ex}\n')

    def read_game_results(self, filename) -> pd.DataFrame:
        try:
            with open(f'{self.__path}/{filename}', 'r', encoding='UTF-8') as file:
                return pd.DataFrame([eval(line.rstrip()) for line in file])
        except FileNotFoundError:
            print(f'Не найден файл с результатами\n')
        except Exception as ex:
            print(f'Произошла ошибка: {ex}\n')
