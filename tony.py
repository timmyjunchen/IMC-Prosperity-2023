import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('61bcb8fd-1630-46c2-857a-db3d51ac73e0.csv', sep = ';')
x = df[df['product'] == 'BANANAS']['timestamp']
y = df[df['product'] == 'BANANAS']['mid_price'].rolling(window = 100).mean()
std = df[df['product'] == 'BANANAS']['mid_price'].rolling(window = 100).std()
BOLU = y + 2 * std
BOLD = y - 2 * std

fig1 = matplotlib.figure.Figure()
ax1 = fig1.add_subplot()
ax1.plot(x, df[df['product'] == 'PEARLS']['mid_price'], color = 'r')
ax1.plot(x, y)
ax1.plot(x, BOLU)
ax1.plot(x, BOLD)

# print(BOLU[len(BOLU) - 1])
# print(BOLD[len(BOLU) - 1])

dfn1 = pd.read_csv('island-data-bottle-round-1/trades_round_1_day_-1_nn.csv', sep=';')
xv = dfn1[dfn1['symbol'] == 'BANANAS']['timestamp']
yv = dfn1[dfn1['symbol'] == 'BANANAS']['quantity'].rolling(window=100).sum()
# xp = dfn1[dfn1['symbol'] == 'PEARLS']['timestamp']
# yp = dfn1[dfn1['symbol'] == 'PEARLS']['quantity'].rolling(window=100).sum()
ax2 = ax1.twinx()
ax2.plot(xv, yv)
# plt.plot(xp, yp, color='r')

fig, ax = plt.subplots()

axes = [ax, ax.twinx()]
axes[1].spines['right'].set_position(('axes', -0.25))
ax.plot(x, y)
ax.set_ylabel('adsklfjsdafkl;')
ax.plot(xv, yv, color='r')
ax.set_ylabel('volume')

plt.show()