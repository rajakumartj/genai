# pip install tradingview-datafeed
import pandas as pd

from tvDatafeed import TvDatafeed,Interval
from datetime import datetime

tv = TvDatafeed()
def get_sec_data(sec_name,bars):
    return tv.get_hist(symbol= sec_name, exchange='NSE', interval=Interval.in_daily, n_bars=bars)


df_data = pd.read_csv("C:/Users/Public/automation/genai/csvops/inputfiles/names3.csv")

name_list = []
rec_date_list = []
buy_price_list = []
for name in df_data.get("REC_SEC"):
    name_list.append(name)
    rec_date_list.append(df_data.get("REC_DT")[0])
    buy_price = ""

    rec_date = datetime.strptime(df_data.get("REC_DT")[0], '%Y-%m-%d').date()
    today_date = datetime.today().strftime("%Y-%m-%d")
    today_date = datetime.strptime(today_date, '%Y-%m-%d').date()
    days_elapsed = (today_date - rec_date).days
    print(days_elapsed)

    print(type(rec_date))
    tv_data = get_sec_data(name,days_elapsed)
    print(len(tv_data))


    for i in range(0,len(tv_data)):
        range_date = (tv_data.index[i]).date()



        if (range_date-rec_date).days >0:
            print("TV Date = " + str((tv_data.index[i]).date()))
            open_price = tv_data["open"].iloc[i]
            close_price = tv_data["close"].iloc[i]

            if buy_price == "":
                buy_price = (open_price + close_price) / 2
                buy_price_list.append(buy_price)



print(len(name_list))
print(len(rec_date_list))
print(len(buy_price_list))
df_all = pd.DataFrame({"REC_SEC": name_list,"REC_DATE": rec_date_list, "BUY_PRICE": buy_price_list} )
df_all.to_csv("price.csv", index=False)







    # tv_df = get_sec_data(name)
    # tv_df.to_csv("values.csv")
    # tv_df = tv_df.sort_index(ascending=False)
    # sec_datatime = tv_df.index[0]
    # print(sec_datatime.date())
    # print(tv_df["close"].iloc[0])













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