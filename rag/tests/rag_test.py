"""
@Time    : 2023/12/31 16:05
@Author  : yangzq80@gmail.com
@File    : rag_test.py
"""

import time
from loguru import logger
from rag.rag.indexing.embed.bge import save_chunks2vector
from rag.rag.indexing.load.load_docs import load_pdf
from rag.rag.indexing.split.split_docs import split_docs
from rag.rag.indexing.store.vector_milvus import get_milvus_db

collection_name = 'col2'
db = get_milvus_db(collection_name)

def load_split_store(collection_name:str):
    docs = load_pdf('rag/tests/source_data/ChatGLM + LangChain实践培训.pdf')

    chunks = split_docs(docs)

    logger.info(f'split chunks:{len(chunks)}')

    # for d in chunks:
    #     logger.info(d)

    vector_db = save_chunks2vector(chunks,collection_name)

    query = "微调适应场景"
    docs = vector_db.similarity_search(query)
    print(docs[0].page_content)

def query_vector(query):
    # 存储嵌入的数据和执行矢量搜索


    # docs = db.similarity_search(query)
    # logger.info(docs[0].page_content)
    start = time.time()
    retriever = db.as_retriever(search_kwargs={"k": 1})
    docs = retriever.get_relevant_documents(query)
    logger.info(f'{"*"*10} search cost :{time.time()-start}')

    for o in docs:
        logger.info(o)


def main():
    # load_split_store(collection_name)
    query_vector('给出概要')
    query_vector('vue')
    query_vector('什么是VUE')
    query_vector('作者介绍')


if __name__ == '__main__':
    main()