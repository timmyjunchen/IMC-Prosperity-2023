from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
import pandas as pd

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
            if product.lower() == 'bananas':
                orders: list[Order] = []
                # Get trades from last trading state and add it to prev_market_trade_prices list
                trade_price = []
                
                for i in state.market_trades[product]:
                    trade_price.append(i.price())
                
                # Calculate average of prices in last cycle
                prev_prices_avg =  pd.Series(trade_price).mean()

                bananas_series = pd.Series(self.bananas)
                BOLU = 1.5 * bananas_series.std() + bananas_series.mean()
                BOLD = bananas_series.mean() - 1.5 * bananas_series.std()
                
                if (prev_prices_avg > BOLU):
                    # Sell whatever products we have (may not be fulfilled)
                    # Sell the products at BOLU
                    orders.append(Order(product, BOLU, -20))
                elif (prev_prices_avg < BOLD):
                    # Buy whatever products are available (if there are any) below BOLD
                    orders.append(Order(product, BOLD, 20))
                
                # Pop first value and add new value to end
                self.next_banana_iteration(prev_prices_avg)
                # Add all the above orders to the result dict
                result[product] = orders
            
            if product.lower() == 'pearls':
                orders: list[Order] = []
                # Get trades from last trading state and add it to prev_market_trade_prices list
                trade_price = []
                
                for i in state.market_trades[product]:
                    trade_price.append(i.price())
                
                # Calculate average of prices in last cycle
                prev_prices_avg =  pd.Series(trade_price).mean()

                pearl_series = pd.Series(self.pearls)
                BOLU = 2 * pearl_series.std() + pearl_series.mean()
                BOLD = pearl_series.mean() - 2 * pearl_series.std()
                
                if (prev_prices_avg > BOLU):
                    # Sell whatever products we have (may not be fulfilled)
                    # Sell the products at BOLU
                    orders.append(Order(product, BOLU, -20))
                elif (prev_prices_avg < BOLD):
                    # Buy whatever products are available (if there are any) below BOLD
                    orders.append(Order(product, BOLD, 20))
                
                # Pop first value and add new value to end
                self.next_pearl_iteration(prev_prices_avg)
                # Add all the above orders to the result dict
                result[product] = orders

        return result