import os
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import OpenAI

SERP_API_KEY = ""
os.environ["SERPAPI_API_KEY"] = SERP_API_KEY
OPENAI_API_KEY = ""
client = OpenAI(api_key=OPENAI_API_KEY)
#
tools = load_tools(["serpapi"])

