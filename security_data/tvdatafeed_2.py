# pip install tradingview-datafeed
import pandas as pd

from tvDatafeed import TvDatafeed,Interval
from datetime import datetime

tv = TvDatafeed()
def get_sec_data(sec_name):
    return tv.get_hist(symbol= sec_name, exchange='NSE', interval=Interval.in_daily, n_bars=2)


df_data = pd.read_csv("C:/Users/Public/automation/genai/csvops/inputfiles/names2.csv")

for name in df_data.get("Name"):
    sec_date = datetime.strptime(df_data.get("Date")[0], '%Y-%m-%d').date()

    print(sec_date)
    tv_df = get_sec_data(name)
    tv_df.to_csv("values.csv")
    tv_df = tv_df.sort_index(ascending=False)
    sec_datatime = tv_df.index[0]
    print(sec_datatime.date())
    print(tv_df["close"].iloc[0])













# tv = TvDatafeed()
# stock_data  = tv.get_hist(symbol='TATAMOTORS',exchange='NSE',interval=Interval.in_daily,n_bars=5)
# print(stock_data)
# for day_index in range(len(stock_data)-1):
#     print(stock_data["symbol"].iloc[day_index])
#     print(stock_data["open"].iloc[day_index])
#     print(stock_data["low"].iloc[day_index])
#     print(stock_data["high"].iloc[day_index])
#     print(stock_data["close"].iloc[day_index])
#     print(stock_data["volume"].iloc[day_index])