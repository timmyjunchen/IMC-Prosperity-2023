import numpy as np
import pandas as pd

df_day0 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_-2.csv', sep = ';')
df_day1 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_-1.csv', sep = ';')
df_day2 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_0.csv', sep = ';')

df_day1['timestamp'] = df_day1['timestamp'] + 999900
df_day2['timestamp'] = df_day2['timestamp'] + 2 * 999900

df = pd.concat([df_day0, df_day1, df_day2], axis=0)


