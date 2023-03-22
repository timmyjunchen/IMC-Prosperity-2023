import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import aayush as a

def dumb_punting_algorithm():
    for product in a.state.order_depths.keys():
        if a.product.lower() == 'pearls':
            pass
        if a.product.lower() == 'bananas':
            prev_price = a.state.market_trades[product][-2].price()
            now_price = a.state.market_trades[product][-1].price()
            if now_price < prev_price:
                best_ask = min(a.order_depth.sell_orders.keys())
                best_ask_volume = a.order_depth.sell_orders[best_ask]
                if (best_ask < prev_price):
                    a.orders.append(a.Order(product, best_ask, -best_ask_volume))
            elif now_price > prev_price:
                best_bid = max(a.order_depth.buy_orders.keys())
                best_bid_volume = a.order_depth.buy_orders[best_bid]
                if best_bid > prev_price:
                    a.orders.append(a.Order(product, best_bid, best_bid_volume))





df = pd.read_csv('prices_round_1_day_-1.csv', sep = ';')
x = df[df['product'] == 'PEARLS']['timestamp']
y = df[df['product'] == 'PEARLS']['mid_price'].rolling(window = 100).mean()
std = df[df['product'] == 'PEARLS']['mid_price'].rolling(window = 100).std()
BOLU = y + 2 * std
BOLD = y - 2 * std

# print(BOLU[len(BOLU) - 1])
# print(BOLD[len(BOLU) - 1])

dfn1 = pd.read_csv('trades_round_1_day_-1_nn.csv', sep=';')
xv = dfn1[dfn1['symbol'] == 'PEARLS']['timestamp']
yv = dfn1[dfn1['symbol'] == 'PEARLS']['quantity'].rolling(window=100).sum()

fig, ax = plt.subplots()

ax.plot(x, y, color='b')
ax.set_xlabel('timestamp')
ax.set_ylabel('price')
ax2 = ax.twinx()
ax2.plot(xv, yv, color='r')
ax2.set_ylabel('volume')

plt.show()