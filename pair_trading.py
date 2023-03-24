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
        orders = {}
        for product in state.order_depths.keys():
            
            if product == 'PINA_COLADAS' or product=='COCONUTS':
                
                orders: list[Order] = []
                # Get trades from last trading state and add it to prev_market_trade_prices list
                trade_price_pc = []
                trade_price_c = []

                for i in state.market_trades.get('PINA_COLADAS'):
                    trade_price_pc.append(i.price)
                
                for j in state.market_trades.get('COCONUTS'):
                    trade_price_c.append(i.price)
                
                # Calculate average of prices in last cycle
                prev_prices_avg_pc =  pd.Series(trade_price_pc).mean()
                                
                prev_prices_avg_c =  pd.Series(trade_price_c).mean()
                
                curr_ratio = prev_prices_avg_pc / prev_prices_avg_c

                pina_colada_series = pd.Series(self.pinacolada)
                coconut_series = pd.Series(self.coconuts)

                avg_ratio = pina_colada_series / coconut_series


                BOLU = 2 * avg_ratio.std() + avg_ratio.mean()
                BOLD = avg_ratio.mean() - 2 * avg_ratio.std()
                
                if (curr_ratio > BOLU):
                    # Sell whatever products we have (may not be fulfilled)
                    # Sell the products at BOLU
                    orders.append(Order('PINA_COLADAS', BOLU, -20))

                elif (curr_ratio < BOLD):
                    # Buy whatever products are available (if there are any) below BOLD
                    orders.append(Order('PINA_COLADAS', BOLD, 20))
                
                # Pop first value and add new value to end
                self.next_banana_iteration(prev_prices_avg)
                
                # Add all the above orders to the result dict
                result['PINA_COLADAS'] = orders
            
            if product == 'BANANAS':
                pass
            
            if product == 'PEARLS':
                pass

        logger.flush(state, orders)
        return orders