from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

my_api_key = ""
client = OpenAI(api_key=my_api_key)

prompt_template_name = PromptTemplate(
    input_variables=["country"],
    template="Can you tel me the capital of {country}?"
)
prompt = prompt_template_name.format(country="India")


response = client.invoke(prompt)
print(response)





