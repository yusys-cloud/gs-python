
from langchain.vectorstores import Milvus
from rag.constants import MILVUS_CONNECTION_ARGS

from rag.rag.indexing.embed.bge import get_model

def get_milvus_db(collection_name:str):
    vector_db = Milvus(
        get_model(),
        connection_args= MILVUS_CONNECTION_ARGS,
        collection_name= collection_name,
    )
    return vector_db