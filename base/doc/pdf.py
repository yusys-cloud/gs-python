from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("ChatGLM-LangChain.pdf")
pages = loader.load_and_split()
print(pages)
