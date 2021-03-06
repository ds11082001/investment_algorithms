from abc import ABC
import pandas as pd
from broker import Broker, Action


class Trader(ABC):
    def __init__(self, broker: Broker):
        self.broker = broker

    def process_data(self, data: pd.Series, current_money: float, price: float) -> None:
        raise NotImplementedError

    def start_trading(self):
        for row, current_money, price in self.broker.process_data():
            self.process_data(row, current_money, price)
