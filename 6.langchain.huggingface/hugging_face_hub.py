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
from langchain.chains import LLMChain
from langchain_community.llms.huggingface_hub import HuggingFaceHub

os.environ['HUGGINGFACEHUB_API_TOKEN'] = Keys.HUGGINGFACEHUB_API_TOKEN.value

prompt = PromptTemplate(
    input_variables=["product"],
    template="tell me the top 1 {product} maker in India?")

chain = LLMChain(llm=HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={'temperature':0}),prompt=prompt)

print(chain.run("Camera"))
