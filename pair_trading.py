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
        self.coconuts = [7925.5, 7925.5, 7925.5, 7926.0, 7927.0, 7927.5, 7928.0, 7927.5, 7926.0, 7926.5, 7926.0, 7925.5, 7922.5, 7924.0, 7924.0, 7925.0, 7924.5, 7925.5, 7925.5, 7925.0, 7925.5, 7926.0, 7924.5, 7924.0, 7924.5, 7923.5, 7923.0, 7924.5, 7924.0, 7923.5, 7923.5, 7924.5, 7926.0, 7926.0, 7928.0, 7927.5, 7927.5, 7926.5, 7926.0, 7926.5, 7925.5, 7925.5, 7923.5, 7924.5, 7924.5, 7924.5, 7925.0, 7924.0, 7924.5, 7923.5]
        self.pinacolada = [14856.5, 14856.5, 14857.5, 14857.5, 14855.5, 14855.5, 14856.5, 14856.5, 14855.5, 14854.5, 14853.5, 14853.0, 14848.0, 14849.5, 14848.5, 14849.5, 14851.5, 14853.5, 14856.5, 14853.5, 14854.5, 14853.0, 14849.5, 14847.5, 14850.5, 14848.0, 14849.5, 14852.5, 14852.5, 14851.5, 14853.0, 14851.0, 14849.5, 14850.5, 14853.5, 14853.5, 14855.5, 14854.5, 14851.5, 14854.5, 14853.5, 14849.5, 14849.5, 14851.5, 14852.5, 14850.5, 14854.0, 14851.0, 14850.5, 14851.5]
        
    def next_banana_iteration (self, price):
        self.bananas.append(price)
        self.bananas.pop(0)

    def next_pearl_iteration (self, price):
        self.pearls.append(price)
        self.pearls.pop(0)
    
    def next_coconuts_iteration (self, price):
        self.coconuts.append(price)
        self.coconuts.pop(0)
    
    def next_pinacolada_iteration(self, price):
        self.pinacolada.append(price)
        self.pinacolada.pop(0)
    
    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        result = {}
        for product in state.order_depths.keys():
            
            if product == 'PINA_COLADAS' or product=='COCONUTS':
                
                orders_pc: list[Order] = []
                orders_c: list[Order] = []

                # Get trades from last trading state and add it to prev_market_trade_prices list
                trade_price_pc = []
                trade_price_c = []

                for i in state.market_trades.get('PINA_COLADAS'):
                    trade_price_pc.append(i.price)
                
                for i in state.market_trades.get('COCONUTS'):
                    trade_price_c.append(i.price)
                
                # Calculate average of prices in last cycle
                prev_prices_avg_pc =  pd.Series(trade_price_pc).mean()
                                
                prev_prices_avg_c =  pd.Series(trade_price_c).mean()
                
                curr_ratio = prev_prices_avg_pc / prev_prices_avg_c

                pina_colada_series = pd.Series(self.pinacolada)
                coconut_series = pd.Series(self.coconuts)

                avg_ratio = pina_colada_series / coconut_series

                BOLU = 1.5 * avg_ratio.std() + avg_ratio.mean()
                BOLD = avg_ratio.mean() - 1.5 * avg_ratio.std()
                
                if (prev_prices_avg_c > BOLU):
                    # Sell whatever products we have (may not be fulfilled)
                    # Sell the products at BOLU
                    orders_pc.append(Order('PINA_COLADAS', BOLU, -50))
                    orders_c.append(Order('COCONUTS', BOLU, -50))

                elif (prev_prices_avg_c < BOLD):
                    # Buy whatever products are available (if there are any) below BOLD
                    orders_pc.append(Order('PINA_COLADAS', BOLD, 50))
                    orders_c.append(Order('COCONUTS', BOLD, 50))
                
                # Pop first value and add new value to end
                self.next_pinacolada_iteration(prev_prices_avg_pc)
                self.next_coconuts_iteration(prev_prices_avg_c)

                # Add all the above orders to the result dict
                result['PINA_COLADAS'] = orders_pc
                result['COCONUTS'] = orders_c
            
            if product == 'BANANAS':
                orders: list[Order] = []
                # Get trades from last trading state and add it to prev_market_trade_prices list
                trade_price = []
                
                for i in state.market_trades.get('BANANAS'):
                    trade_price.append(i.price)
                
                # Calculate average of prices in last cycle
                prev_prices_avg =  pd.Series(trade_price).mean()

                bananas_series = pd.Series(self.bananas)
                BOLU = 1.5 * bananas_series.std() + bananas_series.mean()
                BOLD = bananas_series.mean() - 1.5 * bananas_series.std()
                
                if (prev_prices_avg > BOLU):
                    # Sell whatever products we have (may not be fulfilled)
                    # Sell the products at BOLU
                    orders.append(Order('BANANAS', BOLU, -10))
                elif (prev_prices_avg < BOLD):
                    # Buy whatever products are available (if there are any) below BOLD
                    orders.append(Order('BANANAS', BOLD, 10))
                
                # Pop first value and add new value to end
                self.next_banana_iteration(prev_prices_avg)
                # Add all the above orders to the result dict
                result['BANANAS'] = orders
            
            if product == 'PEARLS':
                orders: list[Order] = []
                # Get trades from last trading state and add it to prev_market_trade_prices list
                trade_price = []
                
                for i in state.market_trades.get('PEARLS'):
                    trade_price.append(i.price)
                
                # Calculate average of prices in last cycle
                prev_prices_avg =  pd.Series(trade_price).mean()


                pearl_series = pd.Series(self.pearls)
                BOLU = 0.5 * pearl_series.std() + pearl_series.mean()
                BOLD = pearl_series.mean() - 0.5 * pearl_series.std()
                
                if (prev_prices_avg > BOLU):
                    # Sell whatever products we have (may not be fulfilled)
                    # Sell the products at BOLU
                    orders.append(Order('PEARLS', BOLU, -10))
                elif (prev_prices_avg < BOLD):
                    # Buy whatever products are available (if there are any) below BOLD
                    orders.append(Order('PEARLS', BOLD, 10))
                
                # Pop first value and add new value to end
                self.next_pearl_iteration(prev_prices_avg)
                # Add all the above orders to the result dict
                result['PEARLS'] = orders
 

        logger.flush(state, result)
        return result