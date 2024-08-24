# Serp api is open source. It can connect to multiple api. You can access Open Ai as well
# SerpApi is a real-time API to access Google search results and from others like bing, wikipedia. We handle proxies, solve captchas, and parse all rich structured data for you.
# Real time information can be accessed
# pip install google-search-results
# Generate serp api key from https://serpapi.com/

from langchain.agents import AgentType
from langchain.agents import load_tools
# from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent

# from langchain.llms import OpenAI
from langchain_openai import OpenAI

SERP_API_KEY = ""
OPENAI_API_KEY = ""
client = OpenAI(api_key=OPENAI_API_KEY)

# tool = load_tools(["serpapi"], serpapi_api_key=SERP_API_KEY, llm=client)
# agent = initialize_agent(tool, client, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# response = agent.invoke("who won the recent world cup?")
# print(response)


