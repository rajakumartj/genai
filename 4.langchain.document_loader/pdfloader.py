# pip install pypdf, langchain, openai

from langchain_community.document_loaders import PyPDFLoader

from keys import Keys

loader = PyPDFLoader(r"C:\Users\admin\Desktop\Car_Insurance_2024-25.pdf")
pages = loader.load_and_split()
print(pages)

print(Keys.SERP_API_KEY.value)
print(Keys.OPENAI_API_KEY.value)

def read_file(file):
    try:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extractText()
        return text
    except Exception as e:
        raise Exception("error reading the pdf file")

