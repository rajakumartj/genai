# Langchain is the wrapper on OpenAI
# It provides capability to access various models. It has access to multiple  API
# you can access private data sources
# It is open source.


from langchain_openai import OpenAI

my_api_key = ""
client = OpenAI(api_key=my_api_key)

my_prompt = ""
# my_prompt = "How many countries are there in Asia? and list the top 10 counties"
my_prompt = "What is the capital of India"


response = client.invoke(my_prompt)
print(response)




