# from transformers import AutoTokenizer, AutoModel
# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
# model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
# # cpu部署，内存不足
# # model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4",trust_remote_code=True).float()

# model = model.eval()
# response, history = model.chat(tokenizer, "你好", history=[])
# print(response)

from transformers import AutoTokenizer, AutoModel
# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("/home/ubuntu/yzq/models/chatglm-6b/tokenizer", trust_remote_code=True)
# tokenizer.save_pretrained("/home/ubuntu/yzq/models/chatglm-6b/tokenizer")

# model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
model = AutoModel.from_pretrained("/home/ubuntu/yzq/models/chatglm-6b/models",trust_remote_code=True).half().cuda()
# model.save_pretrained("/home/ubuntu/yzq/models/chatglm-6b/models")

response, history = model.chat(tokenizer, "你好，介绍下go功能特点", history=[])
print(response)
response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
print(response)
