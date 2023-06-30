import re

def parse_insert_sql(sql):
    pattern = r"INSERT INTO .*? VALUES \((.*?)\)"
    match = re.search(pattern, sql)
    if match:
        values_str = match.group(1)
        values = re.findall(r"'((?:[^'\\]|\\.)*)'", values_str)
        return values
    return []

# 读取 biz.sql 文件
with open('/home/ubuntu/yzq/gs-python/base/biz.sql', 'r') as file:
    sql_content = file.read()

# 提取 SQL INSERT 语句
insert_sql_pattern = r"INSERT INTO .*?;"
insert_sql_list = re.findall(insert_sql_pattern, sql_content)

# 解析并打印每个 SQL INSERT 语句的字段值
for insert_sql in insert_sql_list:
    parsed_values = parse_insert_sql(insert_sql)
    for value in parsed_values:
        print(value)
    print('-' * 50)  # 分隔每个 INSERT 语句的解析结果