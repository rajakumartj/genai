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
five_per_up_price_days_list = []
ten_per_up_price_days_list = []
rec_date_index = 0
for name in df_data.get("REC_SEC"):
    name_list.append(name)
    rec_date = df_data.get("REC_DT")[rec_date_index]
    rec_date_list.append(rec_date)
    buy_price = ""
    five_per_up_price_days = ""
    ten_per_up_price_days = ""

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
                buy_price = format(buy_price,".2f")
                buy_price_list.append(buy_price)


            five_per_up_price = 1.05 * float(buy_price)
            if five_per_up_price_days =="":
                if close_price > five_per_up_price:
                    five_per_up_price_days = (range_date-rec_date).days
                    five_per_up_price_days_list.append(five_per_up_price_days)

            ten_per_up_price = 1.10 * float(buy_price)
            if ten_per_up_price_days == "":
                if close_price > ten_per_up_price:
                    ten_per_up_price_days = (range_date - rec_date).days
                    ten_per_up_price_days_list.append(ten_per_up_price_days)

    if five_per_up_price_days=="":
        five_per_up_price_days_list.append("N/A")
    if ten_per_up_price_days=="":
        ten_per_up_price_days_list.append("N/A")




    # print(len(name_list))
    # print(len(rec_date_list))
    # print(len(buy_price_list))
    # print(len(five_per_up_price_days_list))
    # print(len(ten_per_up_price_days_list))

    df_all = pd.DataFrame({"REC_SEC": name_list,"REC_DATE": rec_date_list, "BUY_PRICE": buy_price_list,
                           "5PCR_UP_DATE": five_per_up_price_days_list,
                           "10PCR_UP_DATE": ten_per_up_price_days_list
                           } )
    df_all.to_csv("price.csv", index=False)

    rec_date_index = rec_date_index + 1

