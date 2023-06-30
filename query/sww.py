import re
import requests

# 发起GET请求
url = 'http://api/api/search'
params = {
    'b': 'logs',
    'k': 'sww',
    'key': 'v.msg',
    'value': '学习结束',
    'relation': 'like'
}

response = requests.get(url, params=params)
data = response.json()

# 提取时间和内容
result = []
items = data['data']['items']
for item in items:
    k = item['k']
    v = item['v']
    time = v['time']
    content = v['msg']

    msg = item['v']['msg']
    match = re.search(r'\[(.*?)\]', msg)
    if match:
        number = match.group(1)
        result.append((time, number))

# 将结果输出到文本文件
output_file = 'output.txt'
with open(output_file, 'w') as file:
    for time, content in result:
        file.write(f'Time: {time}')
        file.write(f' Content: {content}\n')

print('提取结果已保存到', output_file)
