import os
from langchain_community.utilities import SerpAPIWrapper
SERP_API_KEY = ""
os.environ["SERPAPI_API_KEY"] = SERP_API_KEY

search = SerpAPIWrapper()
response = search.run("Who won t20 cricket world 2024?")
print(response)
