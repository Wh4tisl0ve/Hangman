from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write_file(self):
        pass


class TxtFileWriter(Writer):
    def write_file(self):
        with open('game_result.txt', 'w') as f:
            f.write('Hello \n World')