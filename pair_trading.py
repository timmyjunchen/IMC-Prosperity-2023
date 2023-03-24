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
            if product == 'PINA_COLADAS':
                pass
            
            if product == 'COCONUTS':
                pass
            
            if product == 'BANANAS':
                pass
            
            if product == 'PEARLS':
                pass

        logger.flush(state, orders)
        return orders