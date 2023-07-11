## Transformers 
提供了数以千计的预训练模型，支持 100 多种语言的文本分类、信息抽取、问答、摘要、翻译、文本生成。它的宗旨是让最先进的 NLP 技术人人易用

- [用 BART 做文本摘要](./transformers/bart-large-cnn.py)
- [transformers演示](https://github.com/huggingface/transformers/blob/main/README_zh-hans.md)

## ChatGLM
[web_demo](./llms/chatglm/web_demo.py) 

## Snippets

```
pip freeze > requirements.txt
```

```
nohup ./auto-run --path=../gs-python/conf/run-starcoder.json &
nohup ./auto-run --path=../gs-python/conf/run-chatglm-6b.json &
```

##  ChatGLM-6B
pip install protobuf==3.20.0 transformers==4.27.1 icetk cpm_kernels

## venv
python3 -m venv venv
source venv/bin/activate

## 错误处理
- requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer')) 重试多次可自动模型下载
