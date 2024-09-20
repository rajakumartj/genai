# pip install nsepy
# pip install datetime
import nsepy as nse
from datetime import date

my_stock_price = nse.get_history(symbol='NIFTY', index=True, start=date(2024,1,16), end=date(2024,9, 17))

print(my_stock_price)
# print(my_stock_price["Open"].iloc[0])

# print(nse.live.getworkingdays(date(2024,9,10), date(2024,9, 15)))
# print(nse.live.get_quote(symbol='INFY'))
#