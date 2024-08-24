# pip install pypdf, langchain, openai, faiss-cpu
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
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
embeddings = OpenAIEmbeddings()
# print(embeddings)

document_search = FAISS.from_texts(texts, embeddings)
# print(document_search)

# query = "When is the policy going to expire?"
# query = "What is the policy number?"
# query = "What is the broker code?"
# query = "What is the DP name?"

# query = "How many members should have served as Judges?"
query = "Who should attend District Council Meeting?"
docs = document_search.similarity_search(query)



from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI

chain = load_qa_chain(OpenAI(), chain_type="stuff")



input_data = {
    'input_documents': docs,
    'question': query,
}


response = chain.invoke(input=input_data)
print(response.get("input_documents"))
