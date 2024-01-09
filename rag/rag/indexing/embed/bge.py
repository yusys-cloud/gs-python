"""
@Time    : 2023/12/31 18:29
@Author  : yangzq80@gmail.com
@File    : bge.py
"""
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Milvus

from rag.constants import MILVUS_CONNECTION_ARGS,EMBEDDING_MODEL_NAME

def get_model() -> HuggingFaceBgeEmbeddings:
    model = HuggingFaceBgeEmbeddings(
        model_name= EMBEDDING_MODEL_NAME,
        model_kwargs = {'device': 'cuda'},
        encode_kwargs = {'normalize_embeddings': True,"device": "cuda"}, # set True to compute cosine similarity
    )
    return model

def save_chunks2vector(all_splits,collection_name):
     model = get_model()

     milvus_store = Milvus.from_documents(
        all_splits,
        model,
        collection_name = collection_name,
        connection_args= MILVUS_CONNECTION_ARGS,
    )
     
    #  milvus_store = Milvus.from_documents(
    #         all_splits,
    #         embedding = model,
    #         connection_args = MILVUS_CONNECTION_ARGS,
    #         collection_name = collection_name,
    #         # drop_old = True,
    # )
     
     return milvus_store


def main():
    hf = get_model()
    ls = hf.embed_documents(['我的','ads哈哈','你好'])
    print(len(ls))


if __name__ == '__main__':
    main()