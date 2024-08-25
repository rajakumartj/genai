from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from keys import Keys

client = OpenAI(api_key=Keys.OPENAI_API_KEY.value)

prompt_template_name = PromptTemplate.from_template(
    "What is the capital of {country}?"
)

prompt = prompt_template_name.format(country="India")

response = client.invoke(prompt)
print(response)





