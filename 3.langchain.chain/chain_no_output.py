from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


OPENAI_API_KEY = ""
client = OpenAI(api_key=OPENAI_API_KEY)

prompt = PromptTemplate.from_template("tell me the top 1 {product} maker in India?")
chain = LLMChain(llm=client, prompt=prompt)

print(chain.invoke("Cookies"))
