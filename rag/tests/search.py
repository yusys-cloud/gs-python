"""
@Time    : 2024/01/04 15:31
@Author  : yangzq80@gmail.com
@File    : search.py
"""

import os

from loguru import logger
from langchain.embeddings import HuggingFaceBgeEmbeddings

from rag.rag.indexing.embed.milvus_helpers import MilvusHelper


DEFAULT_TABLE = os.getenv("DEFAULT_TABLE", "qa_search")

def do_search(table_name: str, question: str, model: HuggingFaceBgeEmbeddings, milvus_client: MilvusHelper):
    try:
        if not table_name:
            table_name = DEFAULT_TABLE
        feat = model.sentence_encode([question])
        results = milvus_client.search_vectors(table_name, feat, 3)
        vids = [str(x.id) for x in results[0]]
        # questions = mysql_cli.search_by_milvus_ids(vids, table_name)
        distances = [x.distance for x in results[0]]
        return distances
    except Exception as e:
        logger.error(f" Error with search : {e}")


def do_get_answer(table_name, question, mysql_cli):
    try:
        if not table_name:
            table_name = DEFAULT_TABLE
        answer = mysql_cli.search_by_question(question, table_name)
        return answer
    except Exception as e:
        logger.error(f" Error with search by question : {e}")