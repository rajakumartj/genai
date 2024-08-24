from configparser import ConfigParser
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.sequential import SimpleSequentialChain


keys = ConfigParser()
print(keys.read(r'I:/aiml/genai/config.ini'))
# OPENAI_API_KEY = ""
OPENAI_API_KEY = keys.get("API_KEYS", "OPENAI_API_KEY")
print(OPENAI_API_KEY)
client = OpenAI(api_key=OPENAI_API_KEY.strip())

prompt_template_name = PromptTemplate(
    input_variables=["product"],
    template="tell me the top 1 {product} maker in India?")

name_chain = LLMChain(llm=client, prompt=prompt_template_name)

prompt_template_price = PromptTemplate(
    input_variables=["product_type"],
    template="what is the price of the one packet of {product_type} maker in India?")

price_chain = LLMChain(llm=client, prompt=prompt_template_price)
chain = SimpleSequentialChain(chains=[name_chain, price_chain])
print(chain.invoke("Cookies"))