import ccxt
import pandas as pd
from datetime import datetime

def fetch_historical_data(exchange_name, symbol, start_date, end_date):
    exchange = getattr(ccxt, exchange_name)()
    timeframe = '1h'  # Daily timeframe
    
    start_timestamp = exchange.parse8601(start_date)
    end_timestamp = exchange.parse8601(end_date)
    
    all_ohlcv = []
    
    while start_timestamp < end_timestamp:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, start_timestamp)
        all_ohlcv.extend(ohlcv)
        
        if len(ohlcv) == 0:
            break
        
        start_timestamp = ohlcv[-1][0] + exchange.parse_timeframe(timeframe) * 1000

    return all_ohlcv

def save_to_csv(data, filename):
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df.to_csv(filename)

# Set parameters
symbol = 'BTC/USDT'
start_date = '2024-01-01T00:00:00Z'
end_date = '2024-09-30T23:59:59Z'

# Fetch and save data for Binance
binance_data = fetch_historical_data('binance', symbol, start_date, end_date)
save_to_csv(binance_data, 'binance_btcusdt_data.csv')

# Fetch and save data for Coinbase
coinbase_data = fetch_historical_data('coinbase', symbol, start_date, end_date)
save_to_csv(coinbase_data, 'coinbase_btcusdt_data.csv')

print("Data fetching and saving completed.")
