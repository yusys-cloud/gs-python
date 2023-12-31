"""
@Time    : 2023/12/31 16:05
@Author  : yangzq80@gmail.com
@File    : rag_test.py
"""

from loguru import logger
from rag.rag.indexing.embed.bge import save_chunks2vector
from rag.rag.indexing.load.load_docs import load_pdf
from rag.rag.indexing.split.split_docs import split_docs

def main():
    docs = load_pdf('rag/tests/source_data/ChatGLM + LangChain实践培训.pdf')

    chunks = split_docs(docs)

    print(len(chunks))

    # for d in chunks:
    #     logger.info(d)

    vector_db = save_chunks2vector(chunks,'collection_2')

    query = "微调适应场景"
    docs = vector_db.similarity_search(query)
    print(docs[0].page_content)


if __name__ == '__main__':
    main()