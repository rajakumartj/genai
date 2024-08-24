# https://huggingface.co
# Huggingface is used as transformer model to convert text to text, image to text etc.
# pip install huggingface_hub
# pip install transformers
# pip install accelerate
# pip install bitsandybytes
# pip install --upgrade --quiet huggingface_hub

import os
from keys import Keys
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

HUGGINGFACEHUB_API_TOKEN = Keys.HUGGINGFACEHUB_API_TOKEN.value
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

question = "Who won the FIFA World Cup in the year 1994? "

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_length=128,
    temperature=0.5,
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
)

llm_chain = prompt | llm
print(llm_chain.invoke({"question": question}))
