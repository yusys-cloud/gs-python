from transformers import AutoModel
import shutil
import zipfile

# 保存模型
model = AutoModel.from_pretrained("codellama/CodeLlama-7b-Instruct-hf")
save_dir = "./bert_model"
model.save_pretrained(save_dir)

# 压缩模型目录
model_name = "bert-base-uncased"
version = "1.0"
zip_filename = f"{model_name}-{version}.zip"
shutil.make_archive(zip_filename.replace(".zip", ""), "zip", save_dir)

# 删除临时模型目录
shutil.rmtree(save_dir)