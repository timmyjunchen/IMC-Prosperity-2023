import json
from typing import *
import pandas as pd
from datamodel import Order, OrderDepth, TradingState, ProsperityEncoder, Symbol

class Logger:
    def __init__(self) -> None:
        self.logs = ""

    def print(self, *objects: Any, sep: str = " ", end: str = "\n") -> None:
        self.logs += sep.join(map(str, objects)) + end

    def flush(self, state: TradingState, orders: dict[Symbol, list[Order]]) -> None:
        print(json.dumps({
            "state": state,
            "orders": orders,
            "logs": self.logs,
        }, cls=ProsperityEncoder, separators=(",", ":"), sort_keys=True))

        self.logs = ""

logger = Logger()

class Trader:
    
    def __init__(self):
        self.bananas = [4873.0, 4870.5, 4872.0, 4873.0, 4872.5, 4872.5, 4875.5, 4871.5, 4872.0, 4869.5, 4873.0, 4872.5, 4872.5, 4871.0, 4872.0, 4872.5, 4871.5, 4872.5, 4871.5, 4873.0, 4873.5, 4876.0, 4873.5, 4874.0, 4875.5, 4874.0, 4874.0, 4875.5, 4874.5, 4874.5, 4876.5, 4875.0, 4875.0, 4874.5, 4874.5, 4873.0, 4873.5, 4876.5, 4873.5, 4871.5, 4872.5, 4872.0, 4871.5, 4871.5, 4872.0, 4870.5, 4869.5, 4875.5, 4872.5, 4873.0]
        self.pearls = [10000.0, 10000.0, 9999.0, 10000.0, 9999.0, 10001.0, 10000.0, 9999.0, 9999.0, 10000.0, 10001.0, 9997.0, 10001.0, 9999.0, 10000.0, 10000.0, 9997.0, 10003.5, 9998.5, 9997.0, 10000.0, 10000.0, 10000.0, 10000.0, 9997.0, 10001.0, 10003.5, 9997.0, 10000.0, 10000.0, 10001.0, 10001.0, 9997.0, 10000.0, 10003.5, 9999.0, 10000.0, 10000.0, 10003.5, 9999.0, 10003.5, 10001.0, 10000.0, 10000.0, 10000.0, 9998.5, 9999.0, 10000.0, 10000.0, 10000.0]
        self.pearls_quantity = 0
        self.bananas_quantity = 0

    def next_banana_iteration (self, price):
        self.bananas.append(price)
        self.bananas.pop(0)

    def next_pearl_iteration (self, price):
        self.pearls.append(price)
        self.pearls.pop(0)

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        result = {}
        for product in state.order_depths.keys():
            if product == 'BANANAS':
                orders: list[Order] = []
                # Get trades from last trading state and add it to prev_market_trade_prices list
                trade_price = []
                
                for i in state.market_trades.get('BANANAS'):
                    trade_price.append(i.price)

                buy_orders = state.order_depths.get('BANANAS').buy_orders
                sell_orders = state.order_depths.get('BANANAS').sell_orders
                if buy_orders is None or sell_orders is None:
                    break

                buy_keys = state.order_depths['BANANAS'].buy_orders.keys()
                sell_keys = state.order_depths['BANANAS'].sell_orders.keys()

                bid_max = 0
                for i in buy_keys:
                    if i > bid_max:
                        bid_max = i

                ask_min = 1000000
                for i in sell_keys:
                    if i < ask_min:
                        ask_min = i
                
                # Calculate average of prices in last cycle
                # prev_prices_avg =  (bid_max + ask_min)/2
                prev_prices_avg =  pd.Series(trade_price).mean()

                if bid_max == 0 and ask_min == 1000000:
                    prev_prices_avg = self.bananas[-1]
                
                bananas_series = pd.Series(self.bananas)
                exp1 = bananas_series.ewm(span=12, adjust=False).mean()
                exp2 = bananas_series.ewm(span=26, adjust=False).mean()
                macd = pd.DataFrame(exp1- exp2).rename(columns = {'mid_price': 'macd'})
                signal = pd.DataFrame(macd.ewm(span=9, adjust = False).mean()).rename(columns={'macd':'signal'})

                dff = pd.DataFrame()
                dff['macd'] = macd
                dff['signal'] = signal
                dff['indicator'] = dff['macd'] - dff['signal']
                last = dff['indicator'].get(len(dff['indicator']) - 1)
                slast = dff['indicator'].get(len(dff['indicator']) - 2)

                if last > 0 and slast < 0:
                    #MACD goes over. Buy
                    orders.append(Order('BANANAS', prev_prices_avg,20))

                if last < 0 and slast > 0:
                    #sell
                    orders.append(Order('BANANAS', prev_prices_avg, -20))
                
                # add new value to end
                self.next_banana_iteration(prev_prices_avg)
                # Add all the above orders to the result dict
                result['BANANAS'] = orders
            
            if product == 'PEARLS':
                orders: list[Order] = []
                # Get trades from last trading state and add it to prev_market_trade_prices list
                trade_price = []
                
                for i in state.market_trades.get('PEARLS'):
                    trade_price.append(i.price)
                
                buy_orders = state.order_depths.get('PEARLS').buy_orders
                sell_orders = state.order_depths.get('PEARLS').sell_orders
                if buy_orders is None or sell_orders is None:
                    break
                
                buy_keys = state.order_depths['PEARLS'].buy_orders.keys()
                sell_keys = state.order_depths['PEARLS'].sell_orders.keys()
                
                bid_max = 0
                for i in buy_keys:
                    if i > bid_max:
                        bid_max = i

                ask_min = 1000000
                for i in sell_keys:
                    if i < ask_min:
                        ask_min = i
                
                # Calculate average of prices in last cycle
                prev_prices_avg =  (bid_max + ask_min)/2

                if bid_max == 0 and ask_min == 1000000:
                    prev_prices_avg = self.pearls[-1]

                print('Pearl price: ' + str(prev_prices_avg))

                pearl_series = pd.Series(self.pearls)
                BOLU = 0.5 * pearl_series.std() + pearl_series.mean()
                BOLD = pearl_series.mean() - 0.5 * pearl_series.std()
                
                if (prev_prices_avg > BOLU):
                    # Sell whatever products we have (may not be fulfilled)
                    # Sell the products at BOLU
                    orders.append(Order('PEARLS', BOLU, -20))
                elif (prev_prices_avg < BOLD):
                    # Buy whatever products are available (if there are any) below BOLD
                    orders.append(Order('PEARLS', BOLD, 20))
                
                # Pop first value and add new value to end
                self.next_pearl_iteration(prev_prices_avg)
                # Add all the above orders to the result dict
                result['PEARLS'] = orders

        logger.flush(state, orders)
        return result