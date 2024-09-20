from nsetools import Nse

# creating a Nse object
nse = Nse()
print(nse)

# print(nse.get_index_list())



# nse stock code for wipro
code = "wipro"

# getting stock quote
quote = nse.get_quote(code)

# printing quote
# print(quote)