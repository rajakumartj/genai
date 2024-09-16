# pip install tradingview-datafeed
import pandas as pd
from tvDatafeed import TvDatafeed,Interval

pd.DataFrame

tv = TvDatafeed()
stock_data  = tv.get_hist(symbol='TATAMOTORS',exchange='NSE',interval=Interval.in_daily,n_bars=5)
print(stock_data)
for day_index in range(len(stock_data)-1):
    print(stock_data["symbol"].iloc[day_index])
    print(stock_data["open"].iloc[day_index])
    print(stock_data["low"].iloc[day_index])
    print(stock_data["high"].iloc[day_index])
    print(stock_data["close"].iloc[day_index])
    print(stock_data["volume"].iloc[day_index])