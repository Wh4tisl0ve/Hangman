import pandas as pd


class Analyzer:
    def __init__(self, df_results: pd.DataFrame):
        self.__df_results = df_results

    def get_last_five_games(self) -> pd.DataFrame:
        return self.__df_results.sort_values(by='date_game')[:5]

    def get_cnt_wins(self) -> pd.DataFrame:
        return self.__df_results.groupby(by='game_result').agg('count')['hidden_word']