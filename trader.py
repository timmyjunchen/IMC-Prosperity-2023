from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
import pandas as pd


class Trader:
    def __init__(self):
        self.bananas = [4872.5, 4873.0]
        self.pearls = [10000.0, 10000.0]

    def next_banana_iteration (self, price):
        self.bananas.append(price)
        # self.bananas.pop(0)

    def next_pearl_iteration (self, price):
        self.pearls.append(price)
        # self.pearls.pop(0)
    
    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        result = {}
        for product in state.order_depths.keys():
            if product == 'PEARLS':

                # Retrieve the Order Depth containing all the market BUY and SELL orders for PEARLS

                # Initialize the list of Orders to be sent as an empty list
                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []
                trade_price = []

                for i in state.market_trades[product]:
                    trade_price.append(i.price)
                
                # Calculate average of prices in last cycle
                prev_prices_avg =  pd.Series(trade_price).mean()
                now_price = pd.Series(self.pearls).mean()

                if (now_price < prev_prices_avg):
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    if best_ask < prev_prices_avg:
                        orders.append(Order(product, best_ask, best_ask_volume))

                elif now_price > prev_prices_avg:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    if best_bid > prev_prices_avg:
                        orders.append(Order(product, best_bid, -best_bid_volume))

                # Add all the above orders to the result dict
                result[product] = orders
            
            if product == 'BANANAS':
                order_depth: OrderDepth = state.order_depths[product]
                orders: list[Order] = []
                trade_price = []

                for i in state.market_trades[product]:
                    trade_price.append(i.price)
                
                # Calculate average of prices in last cycle
                prev_prices_avg =  pd.Series(trade_price).mean()
                now_price = pd.Series(self.bananas).mean()

                if (now_price < prev_prices_avg):
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    if best_ask < prev_prices_avg:
                        orders.append(Order(product, best_ask, best_ask_volume))

                elif (now_price > prev_prices_avg):
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    if best_bid > prev_prices_avg:
                        orders.append(Order(product, best_bid, -best_bid_volume))

                # Return the dict of orders
                # These possibly contain buy or sell orders for PEARLS
                # Depending on the logic above
        return result