import torch

# 使用第三方库如torch或tensorflow来查看显存大小

if torch.cuda.is_available():
    device = torch.cuda.get_device_properties(0)
    print(f"显存大小: {device.total_memory / 1024 ** 3} GB")
else:
    print("没有可用的GPU")
