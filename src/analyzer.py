from typing import Dict

import pandas as pd


class Analyzer:
    def __init__(self, df_results: pd.DataFrame):
        self.__df_results = df_results
        self.handle_df()

    def handle_df(self) -> None:
        self.__df_results = self.__df_results.replace({-1: 'Поражение', 1: 'Победа'})
        self.__df_results['masked_hidden_word'] = self.__df_results['masked_hidden_word'].apply(lambda x: ''.join(x))

    def get_last_five_games(self) -> pd.DataFrame:
        return self.__df_results.sort_values(by='date_game', ascending=False)[
                   ['hidden_word', 'masked_hidden_word', 'game_result', 'date_game']][:5]

    def get_cnt_wins(self) -> int:
        return len(self.__df_results[self.__df_results['game_result'] == 'Победа'])

    def get_cnt_looses(self) -> int:
        return len(self.__df_results[self.__df_results['game_result'] == 'Поражение'])

    def get_mean_cnt_attempts(self) -> float:
        return self.__df_results['used_letters'].apply(lambda x: len(x)).mean()

    def get_game_results(self) -> Dict:
        return {'cnt_win': self.get_cnt_wins(),
                'cnt_loose': self.get_cnt_looses(),
                'mean_attempts': self.get_mean_cnt_attempts(),
                'last_five_game': self.get_last_five_games()}
