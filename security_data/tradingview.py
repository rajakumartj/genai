# pip install tradingview-ta
from tradingview_ta import TA_Handler, Exchange, Interval

my_stock = TA_Handler(symbol="TATAMOTORS", exchange="NSE", screener="india", interval=Interval.INTERVAL_1_DAY)



# print("Summary ****")
# print(my_stock.get_analysis().summary)
# print("Oscillators *****")
# print(my_stock.get_analysis().oscillators)
# print(my_stock.get_analysis().oscillators.get("RECOMMENDATION"))
# print(my_stock.get_analysis().oscillators.get("COMPUTE").get("RSI"))
#
# print("Indicators ****")
# print(my_stock.get_analysis().indicators)
print("RSI (14) : " + str(my_stock.get_analysis().indicators['RSI']))
# print("Opening price: " + str(my_stock.get_analysis().indicators["open"]))
print("Closing Price: " + str(my_stock.get_analysis().indicators["close"]))
# print("Low : " + str(my_stock.get_analysis().indicators["low"]))
# print("High : " + str(my_stock.get_analysis().indicators["high"]))
# print("Mom :" + str(my_stock.get_analysis().indicators["Mom"]))
print("Percentage Change : " + str(my_stock.get_analysis().indicators["change"]))
#
# print("Moving Averages ******")
# print(my_stock.get_analysis().moving_averages)






