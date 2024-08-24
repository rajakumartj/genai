from langchain_openai import OpenAI
from langchain.chains import ConversationChain


OPENAI_API_KEY = ""
client = OpenAI(api_key=OPENAI_API_KEY)
convo = ConversationChain(llm=OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7))
print(convo.run("Who won the first Cricket Word Cup?"))
print(convo.run("How many years it took India for Independence?"))
print(convo.run("Who was the winning team Captain?"))
print(convo.run("whom it got independence from?"))







