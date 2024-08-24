import os
from langchain.agents import AgentType, create_react_agent
from langchain_openai import OpenAI
from langchain_community.agent_toolkits.load_tools import load_tools

SERP_API_KEY = ""
OPENAI_API_KEY = ""
os.environ["SERPAPI_API_KEY"] = SERP_API_KEY
folder_id = "root"


# llm = OpenAI(temperature=0)
# llm = OpenAI(api_key=OPENAI_API_KEY)
client = OpenAI(api_key=OPENAI_API_KEY)

tools = load_tools(["serpapi"], serpapi_api_key=SERP_API_KEY, llm=client)

agent = create_react_agent(
    tools=tools,
    llm=client,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)

agent.invoke("Search in google drive, who is 'Yann LeCun' ?")