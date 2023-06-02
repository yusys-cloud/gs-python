from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)

# model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
# cpu部署，内存不足
model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4",trust_remote_code=True).float()

model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)