from src import view
from src.file_handlers.write_game_result import TxtFileWriter
from src.game_logic.game import HangmanGame
from src.word_repository import WordRepository


class GameLauncher:
    def __init__(self, word_repository: WordRepository):
        self.__word_repository = word_repository

    def run(self) -> None:
        view.show_menu()
        user_cmd = self.input_cmd_menu()
        self.select_item_menu(user_cmd)

    def select_item_menu(self, cmd) -> None:
        match cmd:
            case 1:
                self.start_new_game()
                self.run()
            case 2:
                exit()
            case _:
                view.show_incorrect_command_error()
                self.run()

    def start_new_game(self) -> None:
        hidden_letter = self.__word_repository.get_random_word()
        game = HangmanGame(hidden_letter)

        while game.check_state_game() == 0:
            view.print_info_board(game.get_info_game())

            input_letter = input('Введите букву -> ').lower()
            if game.is_correct_letter(input_letter):
                game.make_move(input_letter)
            else:
                view.show_incorrect_letter_error()

        TxtFileWriter(game).write_file()
        self.show_end_game_message(game)

    def show_end_game_message(self, game: HangmanGame) -> None:
        if game.check_state_game() == 1:
            view.show_win_message(game.get_hidden_word())
        else:
            view.show_loose_message(game.get_hidden_word())

    def input_cmd_menu(self) -> int:
        choice_user = input('Введите команду -> ')
        if choice_user.isdigit() and len(choice_user) == 1:
            if choice_user in ['1', '2', '3']:
                return int(choice_user)

        return -1
