import yfinance as yf

def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

if __name__ == "__main__":
    data = get_stock_data('AAPL', '2022-01-01', '2023-01-01')
    data.to_csv('stock_data.csv')
