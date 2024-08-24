# https://www.pinecone.io/, raju_


# pip install pypdf, langchain, openai, pinecone-client
# pip install "pinecone-client[grpc]"
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from PyPDF2 import PdfReader
import os
from keys import Keys

# pdfReader = PdfReader(r"C:\Users\admin\Desktop\Car_Insurance_2024-25.pdf")
pdfReader = PdfReader(r"I:\tempraj\temp Toastmasters\Diamond_Club_Criteria-District 98.pdf")

raw_text = ""
for i, page in enumerate(pdfReader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

# print(raw_text)

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=132,
    chunk_overlap=25,
    length_function=len,
)

texts = text_splitter.split_text(raw_text)
print(len(texts))

# **
# Set the open ai key;
# in this version the key is taken from environment variable

os.environ["OPENAI_API_KEY"] = Keys.OPENAI_API_KEY.value
os.environ["PINECONE_API_KEY"] = "53ae73b6-9590-4b67-a224-4144123d8850"
embeddings = OpenAIEmbeddings()
print(embeddings)

index_name = "testing"

vectorstore = PineconeVectorStore.from_texts(texts, embeddings, index_name=index_name)
print(vectorstore)


# query = "When is the policy going to expire?"
# query = "What is the policy number?"
# query = "What is the broker code?"
# query = "What is the DP name?"

# query = "How many members should have served as Judges?"
query = "Who should attend District Council Meeting?"
similar_docs = vectorstore.similarity_search(query)
print(similar_docs)

from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI


chain = load_qa_chain(OpenAI(), chain_type="stuff")

input_data = {
    'input_documents': similar_docs,
    'question': query,
}

response = chain.invoke(input=input_data)
print(response.get("input_documents"))