import deepspeed
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments

# 加载模型  
model = AutoModelForCausalLM.from_pretrained("Salesforce/starcoder")

# 准备DeepSpeed配置
ds_config = {
    "train_batch_size": 32,
    "gradient_clipping": 1.0,
}

# 初始化DeepSpeed Engine
model_engine, _, _, _ = deepspeed.initialize(
    args=args,
    model=model,
    config_params=ds_config,
)

# 加载数据集
dataset = load_dataset("code_search_net", split="train") 

# 定义DeepSpeed优化器
optim = torch.optim.Adam(model_engine.parameters())

# 创建Trainer进行微调
training_args = TrainingArguments(output_dir="./starcoder_finetuned")
trainer = Trainer(
    model=model_engine,
    args=training_args,
    train_dataset=dataset,
    optimizer=optim    
)

# 开始微调  
trainer.train()

# 保存微调后的StarCoder模型
model.save_pretrained("./starcoder_finetuned")