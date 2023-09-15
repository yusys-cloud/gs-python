import re

# 打开本地文件并读取内容
file_path = '/home/ubuntu/yzq/test/xp_func.out'  # 替换为你的文件路径
with open(file_path, 'r') as file:
    text = file.read()

# 正则表达式模式，用于匹配JavaScript函数定义
pattern = r'function\s+[\w]+\s*\([^)]*\)\s*{[^}]*}'

# 使用正则表达式查找匹配的函数定义
matches = re.findall(pattern, text, re.DOTALL)

# 打印匹配的函数定义
for match in matches:
    print('*'*12)
    print(match)