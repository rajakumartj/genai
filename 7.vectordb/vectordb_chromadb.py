import os


from keys import Keys
import chardet

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader


os.environ["OPENAI_API_KEY"] = Keys.OPENAI_API_KEY.value


text_loader_kwargs={'autodetect_encoding': True}
loader = DirectoryLoader(r'C:/Users/Public/automation/genai/new_articles', glob = "./*.txt", loader_cls=TextLoader,loader_kwargs=text_loader_kwargs)
document = loader.load()

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
text = text_splitter.split_documents(document)
# print(text[0].page_content)
print("The number split texts are: " + str(len(text)))

# Creating Chroma database of embedding
from langchain import embeddings
from langchain_chroma import Chroma
# The local database is created in ./db folder
persist_directory = "db"
embedding = OpenAIEmbeddings()
chroma_vectordb = Chroma.from_documents(documents=text,embedding=embedding,persist_directory=persist_directory)

# Persist the db to disc
# chroma_vectordb.persist()
# chroma_vectordb = None

# Now, load the database from the disc and then use it is normal database
chroma_vectordb2 = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
    )
# Make a retriever
retriever = chroma_vectordb2.as_retriever()

docs = retriever.get_relevant_documents("How much money did microsoft raise?")

# It is giving 4 answers by default
print(len(docs))

print(docs[0].page_content)
#
# To set the number of answers other than default 4 (not working properly)
retriever2=chroma_vectordb.as_retriever(search_kwarges={"k":2})
docs2 = retriever2.get_relevant_documents("How much money did microsoft raise?")
print(len(docs2))


# Make a chain
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA

llm=OpenAI(api_key=Keys.OPENAI_API_KEY.value)
print(llm)


qa_chain = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff",
    retriever = retriever,
    return_source_documents = True)


query = "How much money did microsoft raise?"
llm_response = qa_chain(query)
print(llm_response["result"])
print("\n\nSources:")

for source in llm_response["source_document"]:
    print(source.metadata["source"])

# from langchain.chains.question_answering import load_qa_chain
# chain = load_qa_chain(llm, chain_type="stuff")
#
# query = "How much money did microsoft raise?"
# input_data = {
#     'input_documents': docs2,
#     'question': query,
# }
#
# response = chain.invoke(input=input_data)
# print(response)
# print(response.get("input_documents"))





















