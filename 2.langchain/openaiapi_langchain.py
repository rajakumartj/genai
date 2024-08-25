# Langchain is the wrapper on OpenAI
# It provides capability to access various models. It has access to multiple  API
# you can access private data sources
# It is open source.


from langchain_openai import OpenAI
from keys import Keys

client = OpenAI(api_key=Keys.OPENAI_API_KEY.value)

# prompt = ""
# prompt = "How many countries are there in Asia? and list the top 10 counties"
prompt = "What is the capital of India?"


response = client.invoke(prompt)
print(response)




