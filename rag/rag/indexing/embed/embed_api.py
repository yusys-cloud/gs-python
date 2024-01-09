"""
@Time    : 2024/01/05 15:30
@Author  : yangzq80@gmail.com
@File    : embed_api.py
"""
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import uvicorn

from rag.constants import EMBEDDING_MODEL_NAME

# 初始化FastAPI应用
app = FastAPI()

# 加载bge-large-zh模型
model = SentenceTransformer(EMBEDDING_MODEL_NAME)

# 定义请求体模型
class QueryRequest(BaseModel):
    query: str

# 定义响应体模型
class QueryResponse(BaseModel):
    query: str
    embedding: list

# 创建API端点
@app.post("/query")
async def query_embedding(request: QueryRequest):
    # 获取请求中的查询文本
    query = request.query

    # 使用模型获取嵌入
    embedding = model.encode(query, convert_to_tensor=True).tolist()

    # 返回查询结果
    return QueryResponse(query=query, embedding=embedding)

def main():
    uvicorn.run(app, host='0.0.0.0', port=8004)


if __name__ == '__main__':
    main()