# make sure you have accelerate and bitsandbytes installed
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# "bigcode/starcoder"
model_path="/home/ubuntu/yzq/models/starcoder"

tokenizer = AutoTokenizer.from_pretrained(model_path)
# for fp16 replace with  `load_in_8bit=True` with   `torch_dtype=torch.float16`
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", torch_dtype=torch.float16)
print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")