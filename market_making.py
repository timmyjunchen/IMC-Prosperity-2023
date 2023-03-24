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

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        result = {}
        for product in state.order_depths.keys():
            if product == 'PEARLS':
                orders: list[Order] = []
                buy_orders = state.order_depths.get('PEARLS').buy_orders
                sell_orders = state.order_depths.get('PEARLS').sell_orders
                if buy_orders is None or sell_orders is None:
                    break

                buy_orders_keys = list(buy_orders.keys())
                buy_orders_keys.sort(reverse=True)
                sell_orders_keys = list(sell_orders.keys())
                sell_orders_keys.sort()
                if buy_orders_keys is None or sell_orders_keys is None:
                    break
                
                for i in range(min([len(buy_orders_keys), len(sell_orders_keys)])):
                    if buy_orders_keys[i] > sell_orders_keys[i]:
                        print('yay?')
                        orders.append(Order('PEARLS', buy_orders_keys[i], -buy_orders[buy_orders_keys[i]]))
                        orders.append(Order('PEARLS', sell_orders_keys[i], sell_orders[sell_orders_keys[i]]))
                    else:
                        print('UGGHGHG')

                result['PEARLS'] = orders
            
            # if product == 'PEARLS':
            #     orders: list[Order] = []
            #     # Get trades from last trading state and add it to prev_market_trade_prices list
            #     trade_price = []
                
            #     if state.market_trades.get('PEARLS') is None:
            #         continue
                
            #     for i in state.market_trades.get('PEARLS'):
            #         trade_price.append(i.price)
                
            #     # Calculate average of prices in last cycle
            #     prev_prices_avg =  pd.Series(trade_price).mean()

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

        logger.flush(state, orders)
        return result