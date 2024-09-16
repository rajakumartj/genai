import requests
from bs4 import BeautifulSoup
import time

# ticker = 'INFY'
ticker = 'ZOMATO'


nse_url = f'https://www.google.com/finance/quote/{ticker}:NSE?'



response = requests.get(nse_url)
print("Status code = " + str(response.status_code))

soup = BeautifulSoup(response.text,'html.parser')
print(soup)

stock_price_class = 'YMlKec fxKbKc'
stock_price = soup.find(class_=stock_price_class).text.strip()[1:].replace(",","")
stock_price = float(stock_price)
print(stock_price)

stock_up_down_class = 'NydbP VOXKNe'
stock_up_down_value = soup.find(class_="NydbP VOXKNe")
# stock_up_down_value = soup.find('p', attrs={"class": "NydbP VOXKNe", "data-disable-percent-toggl":"false"})
print(stock_up_down_value)
print(stock_up_down_value.text)
print(stock_up_down_value.get_attribute_list("aria-label")[0])


