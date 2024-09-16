import csv
import pandas as pd
from tradingview_ta import TA_Handler, Exchange, Interval


def get_rsi14(stock_name):
    my_stock = TA_Handler(symbol=stock_name, exchange="NSE", screener="india", interval=Interval.INTERVAL_1_DAY, )
    return my_stock.get_analysis().indicators['RSI']


df = pd.read_csv("C:/Users/Public/automation/genai/csvops/inputfiles/names.csv")


name_list = []
rsi_list = []
for name in df.get("Name"):
    # print("Getting the data for " + name)
    rsi14 = get_rsi14(name)
    if rsi14 > 65:
        name_list.append(name)
        rsi_list.append(str(rsi14))

new_df = pd.DataFrame({"Name": name_list, "RSI14": rsi_list})

new_df = new_df.sort_values(by=["RSI14"], ascending=False,ignore_index=True)
print(new_df)