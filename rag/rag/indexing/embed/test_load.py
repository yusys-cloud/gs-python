"""
@Time    : 2024/01/04 15:50
@Author  : yangzq80@gmail.com
@File    : load.py
"""

import sys
import pandas as pd
from config import DEFAULT_TABLE
from loguru import logger
from milvus_helpers import MilvusHelper
from rag.rag.indexing.embed.bge import get_model
from langchain.embeddings import HuggingFaceBgeEmbeddings


# Get the vector of question
def extract_features(file_dir, model):
    try:
        data = pd.read_csv(file_dir)
        question_data = data['question'].tolist()
        answer_data = data['answer'].tolist()
        sentence_embeddings = model.embed_documents(question_data)
        return question_data, answer_data, sentence_embeddings
    except Exception as e:
        logger.error(f" Error with extracting feature from question {e}")
        sys.exit(1)


# Combine the id of the vector and the question data into a list
def format_data(ids, question_data, answer_data):
    data = [(str(i), q, a) for i, q, a in zip(ids, question_data, answer_data)]
    return data


# Import vectors to Milvus and data to Mysql respectively
def do_load(table_name: str, file_dir: str, model: HuggingFaceBgeEmbeddings, milvus_client: MilvusHelper):
    if not table_name:
        table_name = DEFAULT_TABLE
    if not milvus_client.has_collection(table_name):
        milvus_client.create_collection(table_name)
        milvus_client.create_index(table_name)
    question_data, answer_data, sentence_embeddings = extract_features(file_dir, model)
    ids = milvus_client.insert(table_name, sentence_embeddings)
   
    return len(ids)

# def show_dimension(milvus_client):
#     # 确保集合的维度是正确的
#     collection_info = milvus_client.get_collection_info(collection_name='your_collection')
#     logger.info("Collection Dimension:", collection_info['dimension'])

MILVUS_CLI = MilvusHelper()
table_name = 'test1'
bgemodel = get_model()

def test_load():
    
    TOP_K = 3
    question_data, answer_data, sentence_embeddings = extract_features('rag/tests/source_data/example.csv',bgemodel)

    if not MILVUS_CLI.has_collection(table_name):
        MILVUS_CLI.create_collection(table_name)
        MILVUS_CLI.create_index(table_name)
    ids = MILVUS_CLI.insert('test1', sentence_embeddings)

    logger.info('use HuggingFaceBgeEmbeddings')

def test_sarch():


    question = '你好'

    feat = bgemodel.aembed_query(question)
    logger.info(feat)
    results = MILVUS_CLI.search_vectors(table_name, feat, 3)

    print(results)    

def main():
    MILVUS_CLI.show_dimension(table_name)
    # MILVUS_CLI.delete_collection(table_name)
    # test_load()
    test_sarch()


if __name__ == '__main__':
    main()