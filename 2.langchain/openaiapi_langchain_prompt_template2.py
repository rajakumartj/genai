from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

my_api_key = ""
client = OpenAI(api_key=my_api_key)

my_prompt = ""
# my_prompt = "How many countries are there in Asia? and list the top 10 counties"
my_prompt = "What is the capital of India?"

prompt = PromptTemplate.from_template("What is the capital of {country}?")

prompt = prompt.format(country="India")

response = client.invoke(prompt)
print(response)





