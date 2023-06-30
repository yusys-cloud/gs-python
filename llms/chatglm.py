# from transformers import AutoTokenizer, AutoModel
# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
# model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
# # cpu部署，内存不足
# # model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4",trust_remote_code=True).float()

# model = model.eval()
# response, history = model.chat(tokenizer, "你好", history=[])
# print(response)

pretrained_model_name_or_path= "/home/ubuntu/yzq/models/chatglm-6b"
# pretrained_model_name_or_path="THUDM/chatglm-6b"

from transformers import AutoTokenizer, AutoModel
# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path, trust_remote_code=True)
tokenizer.save_pretrained(pretrained_model_name_or_path)

# model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
model = AutoModel.from_pretrained(pretrained_model_name_or_path,trust_remote_code=True).half().cuda()
model.save_pretrained(pretrained_model_name_or_path)

response, history = model.chat(tokenizer, "你好，介绍下go功能特点", history=[])
print(response)
response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
print(response)
