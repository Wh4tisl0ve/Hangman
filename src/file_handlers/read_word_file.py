import os
from typing import List
from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def read_file(self):
        pass


class TxtFileReader(Reader):
    def __init__(self, filename):
        self.__filename = filename

    def read_file(self) -> List[str]:
        try:
            with open(self.__filename, 'r', encoding='UTF-8') as file:
                return file.readlines()
        except FileNotFoundError as file_ex:
            print(f'Файл не найден: {file_ex}\n')
            return self.__find_file()
        except Exception as ex:
            print(f'Произошла ошибка: {ex}\n')

    def __find_file(self) -> List[str]:
        path = 'src/data'
        filename_find = 'russian_nouns.txt'
        print(f'Попытка найти файл в папке {path}/{filename_find}...\n')

        list_files = os.listdir(path)
        if filename_find in list_files:
            self.__filename = os.path.abspath(f'{path}/{filename_find}')
        else:
            print(f'Файл {filename_find} не был найден в {path}')
            self.__filename = input('Введите полный путь к файлу -> ')

        return self.read_file()

