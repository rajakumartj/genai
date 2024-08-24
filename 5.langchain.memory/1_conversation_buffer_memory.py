from langchain_openai import OpenAI
from langchain. prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory


OPENAI_API_KEY = ""
client = OpenAI(api_key=OPENAI_API_KEY.strip())
memory = ConversationBufferMemory()

prompt_template_name = PromptTemplate(
    input_variables=["product"],
    template="tell me the top 1 {product} maker in India?")

# memory_chain = LLMChain(llm=client, prompt=prompt_template_name)
memory_chain = LLMChain(llm=client, prompt=prompt_template_name, memory=memory)
print(memory_chain.invoke("Drone"))
print(memory_chain.invoke("Camera"))
print(memory_chain.invoke("Mobile Phone"))
print(memory.buffer)




