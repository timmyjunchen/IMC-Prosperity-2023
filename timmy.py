import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# df = pd.read_csv('61bcb8fd-1630-46c2-857a-db3d51ac73e0.csv', sep = ';')

df_day0 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_-2.csv', sep = ';')
df_day1 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_-1.csv', sep = ';')
df_day2 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_0.csv', sep = ';')

df_day1['timestamp'] = df_day1['timestamp'] + 999900
df_day2['timestamp'] = df_day2['timestamp'] + 2 * 999900

# df = df_day2.merge(df_day1, on=["day", "timestamp", "product", "bid_price_1","bid_volume_1","bid_price_2","bid_volume_2","bid_price_3","bid_volume_3","ask_price_1","ask_volume_1","ask_price_2","ask_volume_2","ask_price_3","ask_volume_3","mid_price","profit_and_loss"], how='outer')
df = pd.concat([df_day0, df_day1, df_day2], axis=0)
# df.to_csv("final.csv",index=False)

x = df[df['product'] == 'BANANAS']['timestamp']
y = df[df['product'] == 'BANANAS']['mid_price'].rolling(window = 50).mean()
std = df[df['product'] == 'BANANAS']['mid_price'].rolling(window = 50).std()
BOLU = y + 2 * std
BOLD = y - 2 * std

plt.plot(x, df[df['product'] == 'BANANAS']['mid_price'], color = 'r')
#plt.plot(x, y)
plt.plot(x, BOLU)
plt.plot(x, BOLD)
#plt.show()

#print(BOLU[len(BOLU)-2])
#BOLD = BOLD.reset_index()
#print(BOLD['mid_price'][len(BOLD['mid_price']) - 1])
y = df[df['product'] == 'BANANAS']['mid_price']
y = y.reset_index()
print(list(y['mid_price'][len(y) - 50:len(y)]))
y = df[df['product'] == 'PEARLS']['mid_price']
y = y.reset_index()
print(list(y['mid_price'][len(y) - 50:len(y)]))

print()
