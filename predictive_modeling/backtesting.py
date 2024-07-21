import backtrader as bt
import pandas as pd

class TestStrategy(bt.Strategy):
    def __init__(self):
        pass

    def next(self):
        pass

def backtest_strategy():
    cerebro = bt.Cerebro()
    cerebro.addstrategy(TestStrategy)
    data = bt.feeds.PandasData(dataname=pd.read_csv('stock_data.csv'))
    cerebro.adddata(data)
    cerebro.run()

if __name__ == "__main__":
    backtest_strategy()
