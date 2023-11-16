# Gs-Python
Python学习Demo.

- [Code Llama 7B和13B模型用于文本/代码补全或填充](./llms/codellama/)
- [用 BART 做文本摘要](./transformers/bart-large-cnn.py)
- [transformers演示](https://github.com/huggingface/transformers/blob/main/README_zh-hans.md)
- [使用 PyTorch 和 DeepSpeed(training, inference, compression, benchmarks, and applications that use DeepSpeed) 训练屏蔽语言模型](./deepspeed/)
- [一种快速、经济实惠、可扩展且开放的系统框架，可实现端到端强化学习人类反馈 (RLHF) 培训体验，从而生成各种规模的高质量 ChatGPT 式模型。]
- [ChatGLM web_demo](./llms/chatglm/web_demo.py) 
- [GPU信息查看](./base/gpu_info.py) 

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

