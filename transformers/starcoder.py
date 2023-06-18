# pip install -q transformers
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigcode/starcoder"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
tokenizer.save_pretrained("/home/ubuntu/yzq/models/starcoder")

# model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
model = AutoModelForCausalLM.from_pretrained("bigcode/starcoder", device_map="auto", load_in_8bit=True)
# model= AutoModelForCausalLM.from_pretrained("bigcode/starcoder",torch_dtype=torch.float16)
print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")

model.save_pretrained("/home/ubuntu/yzq/models/starcoder")

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
