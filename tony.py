import numpy as np
import pandas as pd

df_day0 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_-2.csv', sep = ';')
df_day1 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_-1.csv', sep = ';')
df_day2 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_0.csv', sep = ';')

df_day1['timestamp'] = df_day1['timestamp'] + 999900
df_day2['timestamp'] = df_day2['timestamp'] + 2 * 999900

df = pd.concat([df_day0, df_day1, df_day2], axis=0)

# bananas = df[df['product'] == 'BANANAS']['mid_price'].reset_index().drop('index', axis=1)
bananas = pd.Series([4873.0, 4870.5, 4872.0, 4873.0, 4872.5, 4872.5, 4875.5, 4871.5, 4872.0, 4869.5, 4873.0, 4872.5, 4872.5, 4871.0, 4872.0, 4872.5, 4871.5, 4872.5, 4871.5, 4873.0, 4873.5, 4876.0, 4873.5, 4874.0, 4875.5, 4874.0, 4874.0, 4875.5, 4874.5, 4874.5, 4876.5, 4875.0, 4875.0, 4874.5, 4874.5, 4873.0, 4873.5, 4876.5, 4873.5, 4871.5, 4872.5, 4872.0, 4871.5, 4871.5, 4872.0, 4870.5, 4869.5, 4875.5, 4872.5, 4873.0])
exp1 = bananas.ewm(span=12, adjust=False).mean()
exp2 = bananas.ewm(span=26, adjust=False).mean()

macd = pd.DataFrame(exp1- exp2).rename(columns = {'mid_price': 'macd'})
signal = pd.DataFrame(macd.ewm(span=9, adjust = False).mean()).rename(columns={'macd':'signal'})

dff = pd.DataFrame()
dff['macd'] = macd
dff['signal'] = signal
dff['indicator'] = dff['macd'] - dff['signal']
last = dff['indicator'].get(len(dff['indicator']) - 1)
slast = dff['indicator'].get(len(dff['indicator']) - 2)

if last > 0 and slast < 0:
    #buy
    pass

if last < 0 and slast > 0:
    #sell
    pass

print(dff['indicator'])
print(last)
print(slast)
