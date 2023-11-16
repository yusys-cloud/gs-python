from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("tmp/ChatGLM-LangChain.pdf")
pages = loader.load_and_split()
print(pages)

for page in pages:
    print("-"*10)
    print(page.page_content)

