from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

modeId='codellama/CodeLlama-7b-Instruct-hf'
tokenizer = AutoTokenizer.from_pretrained(modeId)
model = AutoModelForSeq2SeqLM.from_pretrained(modeId)

tokenizer.save_pretrained("/home/ubuntu/models")
model.save_pretrained("/home/ubuntu/models")


from huggingface_hub import hf_hub_download

hf_hub_download(repo_id="codellama/CodeLlama-7b-Instruct-hf", filename="config.json", cache_dir="/home/ubuntu/models")