import alpaca_trade_api as tradeapi

def execute_trade(symbol, qty, side, type='market', time_in_force='gtc'):
    api = tradeapi.REST('APCA_API_KEY_ID', 'APCA_API_SECRET_KEY', base_url='https://paper-api.alpaca.markets')
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        time_in_force=time_in_force
    )

if __name__ == "__main__":
    execute_trade('AAPL', 10, 'buy')
