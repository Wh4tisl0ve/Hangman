from abc import ABC, abstractmethod
from src.game_logic.game import HangmanGame


class Writer(ABC):
    @abstractmethod
    def write_file(self):
        pass


class TxtFileWriter(Writer):
    def __init__(self, game: HangmanGame):
        self.__current_game = game

    def write_file(self) -> None:
        filename = 'src/data/game_result.txt'
        with open(filename, 'a') as f:
            f.write(str(self.__current_game.get_info_game()) + "\n")
