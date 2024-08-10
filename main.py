from src.game_launcher import GameLauncher
from src.file_handlers.read_word_file import TxtFileReader
from src.word_repository import WordRepository


def main():
    filename = 'src/data/russian_nouns.txt'
    txt_reader = TxtFileReader(filename)
    file = txt_reader.read_file()

    word_repo = WordRepository(file)
    game_launcher = GameLauncher(word_repo)
    game_launcher.run()


if __name__ == '__main__':
    main()
