from typing import Dict

import pandas as pd


class Analyzer:
    def __init__(self, df_results: pd.DataFrame):
        self.__df_results = df_results
        self.handle_df()

    def handle_df(self) -> None:
        self.__df_results = self.__df_results.replace({-1: 'Поражение', 1: 'Победа'})
        self.__df_results['masked_hidden_word'] = self.__df_results['masked_hidden_word'].apply(lambda x: ''.join(x))

    def get_cnt_wins(self) -> int:
        return len(self.__df_results[self.__df_results['game_result'] == 'Победа'])

    def get_cnt_looses(self) -> int:
        return len(self.__df_results[self.__df_results['game_result'] == 'Поражение'])

    def get_mean_cnt_attempts(self) -> float:
        return self.__df_results['used_letters'].apply(lambda x: len(x)).mean()

    def get_mean_len_word(self):
        return self.__df_results[self.__df_results['game_result'] == 'Победа']['hidden_word'].apply(lambda x: len(x)).mean()

    def get_most_common_letter(self) -> str:
        letters = self.__df_results['used_letters'].str.cat()
        letter_counts = pd.Series(list(letters)).value_counts()
        most_common_letter = letter_counts.idxmax()
        return str(most_common_letter)

    def get_game_results(self) -> Dict:
        return {'all_game': self.get_cnt_wins() + self.get_cnt_looses(),
                'cnt_win': self.get_cnt_wins(),
                'cnt_loose': self.get_cnt_looses(),
                'mean_attempts': self.get_mean_cnt_attempts(),
                'mean_len_word': self.get_mean_len_word(),
                'most_common_letter': self.get_most_common_letter()}
