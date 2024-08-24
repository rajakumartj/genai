from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

my_api_key = ""
client = OpenAI(api_key=my_api_key)

my_prompt = ""
# my_prompt = "How many countries are there in Asia? and list the top 10 counties"
my_prompt = "What is the capital of India"

prompt_template_name = PromptTemplate(
    input_variables=["country"],
    template="Can you tel me the capital of {country}?"
)
prompt = prompt_template_name.format(country="India")


response = client.invoke(prompt)
print(response)





