from keys import Keys
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain


memory = ConversationBufferWindowMemory(k=5)
# k = number of the previous conversation to be remembered. When K=1, it does remember the history beyond 1
convo = ConversationChain(llm=OpenAI(openai_api_key=Keys.OPENAI_API_KEY.value, temperature=0.7),memory=memory)

print(convo.run("Who won the first Cricket Word Cup?"))
print(convo.run("How many years it took India for Independence?"))
print(convo.run("Who was the winning team Captain?"))
print(convo.run("whom it got independence from?"))







