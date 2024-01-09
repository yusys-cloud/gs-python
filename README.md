# Gs-Python
Python学习Demo.

- [Code Llama 7B和13B模型用于文本/代码补全或填充](./llms/codellama/)
- [用 BART 做文本摘要](./transformers/bart-large-cnn.py)
- [transformers演示](https://github.com/huggingface/transformers/blob/main/README_zh-hans.md)
- [使用 PyTorch 和 DeepSpeed(training, inference, compression, benchmarks, and applications that use DeepSpeed) 训练屏蔽语言模型](./deepspeed/)
- [一种快速、经济实惠、可扩展且开放的系统框架，可实现端到端强化学习人类反馈 (RLHF) 培训体验，从而生成各种规模的高质量 ChatGPT 式模型。]
- [ChatGLM web_demo](./llms/chatglm/web_demo.py) 
- [GPU信息查看](./base/gpu_info.py)
- [Embedding API服务](./rag/rag/indexing/embed/embed_api.py) 
- [emdedding](./llms/embedding/) 嵌入创建一段文本的矢量表示，我们可以在向量空间中思考文本，并执行语义搜索之类的操作，在向量空间中查找最相似的文本片段。
    - [Embeddings 两种方法：嵌入文档与嵌入查询](./llms/embedding/text_embeddings.py)。 前者采用多个文本作为输入，而后者采用单个文本。 将它们作为两种单独方法的原因是，某些嵌入提供程序对文档（要搜索的）与查询（搜索查询本身）有不同的嵌入方法。
    - Text embedding models
    - 存储和搜索非结构化数据的最常见方法之一是嵌入它并存储生成的嵌入向量，然后在查询时嵌入非结构化查询并检索与嵌入查询“最相似”的嵌入向量。 矢量存储负责存储嵌入数据并为您执行矢量搜索。
    - [milvus使用m3e-base嵌入模型](./llms/vectorstores/milvus.py)
    - Maximum marginal relevance search (MMR) 最大边际相关性搜索
    - [海量文本嵌入基准 (MTEB) 中文排名1：thenlper/gte-large-zh The GTE models are trained by Alibaba DAMO Academy.](./llms/embedding/gte.py)
- [Retrievers] 检索器接受字符串查询作为输入，并返回文档列表作为输出
    - 检索器使用语义相似性和时间衰减的组合。
- [基础文本处理](./base/)
    - [javalang对java进行AST处理](./base/ast/java_method.py)
- [vector database milvus](./rag/rag/indexing/store/hello_milvus.py)
    - 主键可以指定或者默认，主键可以重复,通过主键删除数据
    - Fields组成 entities. 可以是结构化数据 (numbers, strings) or vectors.
    - embedding vector is an array of floating-point numbers or binaries
- [LangChain]

## Snippets
```
pip freeze > requirements.txt
```

## huggingface 
模型下载

```
nohup ./auto-run --path=../gs-python/conf/run-starcoder.json &
nohup ./auto-run --path=../gs-python/conf/run-chatglm-6b.json &
nohup ./auto-run --path=../gs-python/conf/models/lfs-codellama.json &
```

## venv
python3 -m venv venv
source venv/bin/activate

conda env list
conda activate py310

python3 -m pip install easyocr

## 参考
- [使用 BERT 进行文本分类](https://medium.com/@khang.pham.exxact/text-classification-with-bert-7afaacc5e49b)