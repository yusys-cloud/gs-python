import os

############### Milvus Configuration ###############
MILVUS_HOST = os.getenv("MILVUS_HOST", "n3")
MILVUS_PORT = int(os.getenv("MILVUS_PORT", "19530"))
# bge-large-zh模型的向量维度是1024
VECTOR_DIMENSION = int(os.getenv("VECTOR_DIMENSION", "1024"))
INDEX_FILE_SIZE = int(os.getenv("INDEX_FILE_SIZE", "1024"))
METRIC_TYPE = os.getenv("METRIC_TYPE", "IP")
DEFAULT_TABLE = os.getenv("DEFAULT_TABLE", "qa_search")
TOP_K = int(os.getenv("TOP_K", "10"))

############### MySQL Configuration ###############
MYSQL_HOST = os.getenv("MYSQL_HOST", "n1")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PWD = os.getenv("MYSQL_PWD", "llm")
MYSQL_DB = os.getenv("MYSQL_DB", "llm")

############### Data Path ###############
UPLOAD_PATH = os.getenv("UPLOAD_PATH", "tmp/qa-data")

############### Number of log files ###############
LOGS_NUM = int(os.getenv("logs_num", "0"))
