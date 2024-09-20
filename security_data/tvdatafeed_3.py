# pip install tradingview-datafeed
import pandas as pd

from tvDatafeed import TvDatafeed,Interval
from datetime import datetime

tv = TvDatafeed()
def get_sec_data(sec_name,bars):
    return tv.get_hist(symbol= sec_name, exchange='NSE', interval=Interval.in_daily, n_bars=bars)



input_file_name = "C:/Users/Public/automation/genai/security_data/inputfiles/mid_rec.csv"
output_file_name = "C:/Users/Public/automation/genai/security_data/outputfiles/mid_rec_processed.csv"
df_data = pd.read_csv(input_file_name)


name_list = []
rec_date_list = []
buy_price_list = []
five_per_up_price_days_list = []
five_per_up_price_count = 0
ten_per_up_price_days_list = []
per_increase_as_of_today_list = []
price_as_of_today_list = []
ten_per_up_price_count = 0
df_data_row_index = 0

for name in df_data.get("REC_SEC"):
    name_list.append(name)
    print("Security Name ******************************************* = " + name)
    rec_date = df_data.get("REC_DT")[df_data_row_index]
    rec_date_list.append(rec_date)
    buy_price = 0
    five_per_up_price_days = ""
    ten_per_up_price_days = ""

    rec_date = datetime.strptime(df_data.get("REC_DT")[df_data_row_index], '%Y-%m-%d').date()
    today_date = datetime.today().strftime("%Y-%m-%d")
    today_date = datetime.strptime(today_date, '%Y-%m-%d').date()
    days_elapsed = (today_date - rec_date).days
    print(days_elapsed)

    tv_data = get_sec_data(name,days_elapsed)
    print(len(tv_data))


    for i in range(0,len(tv_data)):
        range_date = (tv_data.index[i]).date()

        if (range_date-rec_date).days >0:
            print("TV Date = " + str((tv_data.index[i]).date()))
            open_price = tv_data["open"].iloc[i]
            close_price = tv_data["close"].iloc[i]

            print("Open Price = " + str(open_price))
            print("Close price = " + str(close_price))

            if buy_price == 0:
                buy_price = (open_price + close_price) / 2
                buy_price = format(buy_price,".2f")
                buy_price_list.append(buy_price)


            five_per_up_price = 1.05 * float(buy_price)
            if five_per_up_price_days =="":
                if close_price > five_per_up_price:
                    five_per_up_price_days = (range_date-rec_date).days
                    five_per_up_price_days_list.append(five_per_up_price_days)
                    print("Closing price for 5per up on " + str(range_date) + " was " + str(close_price))
                    five_per_up_price_count = five_per_up_price_count + 1

            ten_per_up_price = 1.10 * float(buy_price)
            if ten_per_up_price_days == "":
                if close_price > ten_per_up_price:
                    ten_per_up_price_days = (range_date - rec_date).days
                    ten_per_up_price_days_list.append(ten_per_up_price_days)
                    print("Closing price for 10 per up on " + str(range_date) + " was " + str(close_price))
                    ten_per_up_price_count = ten_per_up_price_count +1

            if (today_date-range_date).days==0:
                print(close_price)
                per_increase_as_of_today = (close_price-float(buy_price))*100/float(buy_price)
                per_increase_as_of_today = format(per_increase_as_of_today,"0.2f")
                per_increase_as_of_today_list.append(str(per_increase_as_of_today))

                price_as_of_today_list.append(format(float(close_price),".2f"))




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
                           "5PCR_UP_DATE": five_per_up_price_days_list,"10PCR_UP_DATE": ten_per_up_price_days_list,
                           "CURRENT_PRICE": price_as_of_today_list,"PER_CHANGE":per_increase_as_of_today_list
                           }, columns=["REC_SEC","REC_DATE","BUY_PRICE","5PCR_UP_DATE","10PCR_UP_DATE","CURRENT_PRICE","PER_CHANGE"])
    df_all.to_csv(output_file_name, index=False)

    df_data_row_index = df_data_row_index + 1
    if df_data_row_index == 1000:
        exit()
print("Number of securities that are in action  = "  + str(len(df_data)))
print("Number of securities that are up by 5%  = "  + str(five_per_up_price_count))
print("Number of securities that are up by 10%  = "  + str(ten_per_up_price_count))

total_buy_value = 0
for bp in buy_price_list:
    total_buy_value = total_buy_value + float(bp)

total_current_value = 0
for cv in price_as_of_today_list:
    total_current_value = total_current_value + float(cv)
print("Total invested = " + format(total_buy_value,"0.5"))
print("Total current value = " + format(total_current_value,"0.5"))

per_change_value = (total_current_value - total_buy_value)*100/total_buy_value
print("Total % Change " + str(format(per_change_value,".2f")))