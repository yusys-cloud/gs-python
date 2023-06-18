import torch

def get_gpu_info():
    if torch.cuda.is_available():
        device = torch.cuda.current_device()
        gpu_name = torch.cuda.get_device_name(device)
        cuda_version = torch.version.cuda
        cuda_capabilities = torch.cuda.get_device_capability(device)
        total_memory = torch.cuda.get_device_properties(device).total_memory
        memory_allocated = torch.cuda.memory_allocated(device)
        memory_cached = torch.cuda.memory_reserved(device)
        
        print("GPU Name:", gpu_name)
        print("CUDA Version:", cuda_version)
        print("CUDA Capabilities:", cuda_capabilities)
        print("Total GPU Memory:", total_memory / 1024**3, "GB")
        print("Memory Allocated:", memory_allocated / 1024**3, "GB")
        print("Memory Cached:", memory_cached / 1024**3, "GB")
    else:
        print("No GPU available")

# 调用函数获取GPU信息
get_gpu_info()
