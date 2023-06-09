import json
from typing import *
import pandas as pd
from datamodel import Order, OrderDepth, TradingState, ProsperityEncoder, Symbol
            
def round_1():
    # df = pd.read_csv('prices_round_1_day_-1.csv', sep = ';')
    # x = df[df['product'] == 'PEARLS']['timestamp']
    # y = df[df['product'] == 'PEARLS']['mid_price'].rolling(window = 100).mean()
    # std = df[df['product'] == 'PEARLS']['mid_price'].rolling(window = 100).std()
    # BOLU = y + 2 * std
    # BOLD = y - 2 * std

    # print(BOLU[len(BOLU) - 1])
    # print(BOLD[len(BOLU) - 1])

    # dfn1 = pd.read_csv('trades_round_1_day_-1_nn.csv', sep=';')
    # xv = dfn1[dfn1['symbol'] == 'PEARLS']['timestamp']
    # yv = dfn1[dfn1['symbol'] == 'PEARLS']['quantity'].rolling(window=100).sum()

    # fig, ax = plt.subplots()

    # ax.plot(x, y, color='b')
    # ax.set_xlabel('timestamp')
    # ax.set_ylabel('price')
    # ax2 = ax.twinx()
    # ax2.plot(xv, yv, color='r')
    # ax2.set_ylabel('volume')

    # plt.show()
    pass

def round_2():
    pass
    # df_day0 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_-2.csv', sep = ';')
    # df_day1 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_-1.csv', sep = ';')
    # df_day2 = pd.read_csv('./island-data-bottle-round-1/prices_round_1_day_0.csv', sep = ';')

    # df_day1['timestamp'] = df_day1['timestamp'] + 999900
    # df_day2['timestamp'] = df_day2['timestamp'] + 2 * 999900

    # df = pd.concat([df_day0, df_day1, df_day2], axis=0)
    # bananas = df[df['product'] == 'BANANAS']['mid_price']

    # exp1_bananas = bananas.ewm(span=12, adjust=False).mean()
    # exp2_bananas = bananas.ewm(span=26, adjust=False).mean()
    # macd_bananas = pd.DataFrame(exp1_bananas - exp2_bananas).rename(columns = {'mid_price': 'macd'})
    # signal = pd.DataFrame(macd_bananas.ewm(span=9, adjust = False).mean()).rename(columns={'macd':'signal'})

    # df_new = pd.concat([macd_bananas, signal], axis = 1)
    # buy = df_new['macd'] - df_new['signal']
    # buy = buy.reset_index()
    # print(buy[0][len(buy) - 1])

    # ------ Attempted implementation ----- #
    # class Logger:
    #     def __init__(self) -> None:
    #         self.logs = ""

    #     def print(self, *objects: Any, sep: str = " ", end: str = "\n") -> None:
    #         self.logs += sep.join(map(str, objects)) + end

    #     def flush(self, state: TradingState, orders: dict[Symbol, list[Order]]) -> None:
    #         print(json.dumps({
    #             "state": state,
    #             "orders": orders,
    #             "logs": self.logs,
    #         }, cls=ProsperityEncoder, separators=(",", ":"), sort_keys=True))

    #         self.logs = ""

    #     logger = Logger()

    #     class Trader:
            
    #         def __init__(self):
    #             self.bananas = [4873.0, 4870.5, 4872.0, 4873.0, 4872.5, 4872.5, 4875.5, 4871.5, 4872.0, 4869.5, 4873.0, 4872.5, 4872.5, 4871.0, 4872.0, 4872.5, 4871.5, 4872.5, 4871.5, 4873.0, 4873.5, 4876.0, 4873.5, 4874.0, 4875.5, 4874.0, 4874.0, 4875.5, 4874.5, 4874.5, 4876.5, 4875.0, 4875.0, 4874.5, 4874.5, 4873.0, 4873.5, 4876.5, 4873.5, 4871.5, 4872.5, 4872.0, 4871.5, 4871.5, 4872.0, 4870.5, 4869.5, 4875.5, 4872.5, 4873.0]
    #             self.pearls = [10000.0, 10000.0, 9999.0, 10000.0, 9999.0, 10001.0, 10000.0, 9999.0, 9999.0, 10000.0, 10001.0, 9997.0, 10001.0, 9999.0, 10000.0, 10000.0, 9997.0, 10003.5, 9998.5, 9997.0, 10000.0, 10000.0, 10000.0, 10000.0, 9997.0, 10001.0, 10003.5, 9997.0, 10000.0, 10000.0, 10001.0, 10001.0, 9997.0, 10000.0, 10003.5, 9999.0, 10000.0, 10000.0, 10003.5, 9999.0, 10003.5, 10001.0, 10000.0, 10000.0, 10000.0, 9998.5, 9999.0, 10000.0, 10000.0, 10000.0]
    #             self.pearls_quantity = 0
    #             self.bananas_quantity = 0

    #         def next_banana_iteration (self, price):
    #             self.bananas.append(price)
    #             # self.bananas.pop(0)

    #         def next_pearl_iteration (self, price):
    #             self.pearls.append(price)
    #             # self.pearls.pop(0)

    #         def run(self, state: TradingState) -> Dict[str, List[Order]]:
    #             result = {}
    #             for product in state.order_depths.keys():
    #                 if product == 'BANANAS':
    #                     orders: list[Order] = []
    #                     # Get trades from last trading state and add it to prev_market_trade_prices list
    #                     trade_price = []
                        
    #                     for i in state.market_trades.get('BANANAS'):
    #                         trade_price.append(i.price)
                        
    #                     # Calculate average of prices in last cycle
    #                     prev_prices_avg =  pd.Series(trade_price).mean()

    #                     print('Banana price: ' + prev_prices_avg)

    #                     bananas_series = pd.Series(self.bananas)
    #                     exp1_bananas = bananas_series.ewm(span=12, adjust=False).mean()
    #                     exp2_bananas = bananas_series.ewm(span=26, adjust=False).mean()

    #                     macd_bananas = pd.DataFrame(exp1_bananas - exp2_bananas).rename(columns = {'mid_price': 'macd'})
    #                     signal = pd.DataFrame(macd_bananas.ewm(span=9, adjust = False).mean()).rename(columns={'macd':'signal'})

    #                     df = pd.concat([macd_bananas, signal], axis = 1)
    #                     indicator = df['macd_bananas'] - df['signal']
    #                     indicator = indicator.reset_index()
    #                     last_val = indicator[0][len(indicator) - 1]

    #                     if (last_val < 0):
    #                         # Sell whatever products we have (may not be fulfilled)
    #                         orders.append(Order('BANANAS', prev_prices_avg, -20))
    #                     elif (last_val > 0):
    #                         # Buy whatever products are available (if there are any)
    #                         orders.append(Order('BANANAS', prev_prices_avg, 20))
                        
    #                     # Pop first value and add new value to end
    #                     self.next_banana_iteration(prev_prices_avg)
    #                     # Add all the above orders to the result dict
    #                     result['BANANAS'] = orders
    #        

    # from typing import Dict, List
    # from datamodel import OrderDepth, TradingState, Order
    # import pandas as pd


    # class Trader:
    #     def __init__(self):
    #         self.bananas = [4872.5, 4873.0]
    #         self.pearls = [10000.0, 10000.0]

    #     def next_banana_iteration (self, price):
    #         self.bananas.append(price)
    #         # self.bananas.pop(0)

    #     def next_pearl_iteration (self, price):
    #         self.pearls.append(price)
    #         # self.pearls.pop(0)
        
    #     def run(self, state: TradingState) -> Dict[str, List[Order]]:
    #         result = {}
    #         for product in state.order_depths.keys():
    #             if product == 'PEARLS':

    #                 # Retrieve the Order Depth containing all the market BUY and SELL orders for PEARLS

    #                 # Initialize the list of Orders to be sent as an empty list
    #                 order_depth: OrderDepth = state.order_depths[product]
    #                 orders: list[Order] = []
    #                 trade_price = []

    #                 for i in state.market_trades[product]:
    #                     trade_price.append(i.price)
                    
    #                 # Calculate average of prices in last cycle
    #                 prev_prices_avg =  pd.Series(trade_price).mean()
    #                 now_price = pd.Series(self.pearls).mean()

    #                 if (now_price < prev_prices_avg):
    #                     best_ask = min(order_depth.sell_orders.keys())
    #                     best_ask_volume = order_depth.sell_orders[best_ask]
    #                     if best_ask < prev_prices_avg:
    #                         orders.append(Order(product, best_ask, best_ask_volume))

    #                 elif now_price > prev_prices_avg:
    #                     best_bid = max(order_depth.buy_orders.keys())
    #                     best_bid_volume = order_depth.buy_orders[best_bid]
    #                     if best_bid > prev_prices_avg:
    #                         orders.append(Order(product, best_bid, -best_bid_volume))

    #                 # Add all the above orders to the result dict
    #                 result[product] = orders
                
    #             if product == 'BANANAS':
    #                 order_depth: OrderDepth = state.order_depths[product]
    #                 orders: list[Order] = []
    #                 trade_price = []

    #                 for i in state.market_trades[product]:
    #                     trade_price.append(i.price)
                    
    #                 # Calculate average of prices in last cycle
    #                 prev_prices_avg =  pd.Series(trade_price).mean()
    #                 now_price = pd.Series(self.bananas).mean()

    #                 if (now_price < prev_prices_avg):
    #                     best_ask = min(order_depth.sell_orders.keys())
    #                     best_ask_volume = order_depth.sell_orders[best_ask]
    #                     if best_ask < prev_prices_avg:
    #                         orders.append(Order(product, best_ask, best_ask_volume))

    #                 elif (now_price > prev_prices_avg):
    #                     best_bid = max(order_depth.buy_orders.keys())
    #                     best_bid_volume = order_depth.buy_orders[best_bid]
    #                     if best_bid > prev_prices_avg:
    #                         orders.append(Order(product, best_bid, -best_bid_volume))

    #                 # Return the dict of orders
    #                 # These possibly contain buy or sell orders for PEARLS
    #                 # Depending on the logic above
    #         return result

    # ------ Attempted round 2 implementation -------
    # import json
    # from typing import *
    # import pandas as pd
    # from datamodel import Order, OrderDepth, TradingState, ProsperityEncoder, Symbol

    # class Logger:
    #     def __init__(self) -> None:
    #         self.logs = ""

    #     def print(self, *objects: Any, sep: str = " ", end: str = "\n") -> None:
    #         self.logs += sep.join(map(str, objects)) + end

    #     def flush(self, state: TradingState, orders: dict[Symbol, list[Order]]) -> None:
    #         print(json.dumps({
    #             "state": state,
    #             "orders": orders,
    #             "logs": self.logs,
    #         }, cls=ProsperityEncoder, separators=(",", ":"), sort_keys=True))

    #         self.logs = ""

    # logger = Logger()

    # class Trader:
        
    #     def __init__(self):
    #         self.bananas = [4873.0, 4870.5, 4872.0, 4873.0, 4872.5, 4872.5, 4875.5, 4871.5, 4872.0, 4869.5, 4873.0, 4872.5, 4872.5, 4871.0, 4872.0, 4872.5, 4871.5, 4872.5, 4871.5, 4873.0, 4873.5, 4876.0, 4873.5, 4874.0, 4875.5, 4874.0, 4874.0, 4875.5, 4874.5, 4874.5, 4876.5, 4875.0, 4875.0, 4874.5, 4874.5, 4873.0, 4873.5, 4876.5, 4873.5, 4871.5, 4872.5, 4872.0, 4871.5, 4871.5, 4872.0, 4870.5, 4869.5, 4875.5, 4872.5, 4873.0]
    #         self.pearls = [10000.0, 10000.0, 9999.0, 10000.0, 9999.0, 10001.0, 10000.0, 9999.0, 9999.0, 10000.0, 10001.0, 9997.0, 10001.0, 9999.0, 10000.0, 10000.0, 9997.0, 10003.5, 9998.5, 9997.0, 10000.0, 10000.0, 10000.0, 10000.0, 9997.0, 10001.0, 10003.5, 9997.0, 10000.0, 10000.0, 10001.0, 10001.0, 9997.0, 10000.0, 10003.5, 9999.0, 10000.0, 10000.0, 10003.5, 9999.0, 10003.5, 10001.0, 10000.0, 10000.0, 10000.0, 9998.5, 9999.0, 10000.0, 10000.0, 10000.0]
    #         self.pearls_quantity = 0
    #         self.bananas_quantity = 0

    #     def next_banana_iteration (self, price):
    #         self.bananas.append(price)
    #         # self.bananas.pop(0)

    #     def next_pearl_iteration (self, price):
    #         self.pearls.append(price)
    #         # self.pearls.pop(0)

    #     def run(self, state: TradingState) -> Dict[str, List[Order]]:
    #         result = {}
    #         for product in state.order_depths.keys():
    #             if product == 'BANANAS':
    #                 orders: list[Order] = []
    #                 # Get trades from last trading state and add it to prev_market_trade_prices list
    #                 trade_price = []
                    
    #                 for i in state.market_trades.get('BANANAS'):
    #                     trade_price.append(i.price)
                    
    #                 # Calculate average of prices in last cycle
    #                 prev_prices_avg =  pd.Series(trade_price).mean()

    #                 # print('Banana price: ' + str(prev_prices_avg))

    #                 bananas_series = pd.Series(self.bananas)
    #                 exp1_bananas = bananas_series.ewm(span=12, adjust=False).mean()
    #                 exp2_bananas = bananas_series.ewm(span=26, adjust=False).mean()

    #                 macd_bananas = pd.DataFrame(exp1_bananas - exp2_bananas).rename(columns = {'mid_price': 'macd'})
    #                 signal = pd.DataFrame(macd_bananas.ewm(span=9, adjust = False).mean()).rename(columns={'macd':'signal'})

    #                 df = pd.concat([macd_bananas, signal], axis = 1)
    #                 if (df.get('macd_bananas') is not None) and (df.get('signal') is not None):
    #                     indicator = df.get('macd_bananas') - df.get('signal')
    #                     indicator = indicator.reset_index()
    #                     last_val = indicator.get(0).get(len(indicator) - 1)

    #                     if (last_val < 0):
    #                         # Sell whatever products we have (may not be fulfilled)
    #                         orders.append(Order('BANANAS', prev_prices_avg, -20))
    #                     elif (last_val > 0):
    #                         # Buy whatever products are available (if there are any)
    #                         orders.append(Order('BANANAS', prev_prices_avg, 20))
                    
    #                 # Pop first value and add new value to end
    #                 self.next_banana_iteration(prev_prices_avg)
    #                 # Add all the above orders to the result dict
    #                 result['BANANAS'] = orders
    
    # if product == 'PEARLS':
    #     orders: list[Order] = []
    #     # Get trades from last trading state and add it to prev_market_trade_prices list
    #     trade_price = []
        
    #     for i in state.market_trades.get('PEARLS'):
    #         trade_price.append(i.price)
        
    #     # Calculate average of prices in last cycle
    #     prev_prices_avg =  pd.Series(trade_price).mean()

    #     print('Pearl price: ' + prev_prices_avg)

    #     pearl_series = pd.Series(self.pearls)
    #     BOLU = 0.5 * pearl_series.std() + pearl_series.mean()
    #     BOLD = pearl_series.mean() - 0.5 * pearl_series.std()
        
    #     if (prev_prices_avg > BOLU):
    #         # Sell whatever products we have (may not be fulfilled)
    #         # Sell the products at BOLU
    #         orders.append(Order('PEARLS', BOLU, -20))
    #     elif (prev_prices_avg < BOLD):
    #         # Buy whatever products are available (if there are any) below BOLD
    #         orders.append(Order('PEARLS', BOLD, 20))
        
    #     # Pop first value and add new value to end
    #     self.next_pearl_iteration(prev_prices_avg)
    #     # Add all the above orders to the result dict
    #     result['PEARLS'] = orders

    #         logger.flush(state, orders)
    #         return result

def round3():
    pass