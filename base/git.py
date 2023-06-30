data = '''
aa====git@192.168.1.21:aa.git====dev_1.4.1====service
bb====git@192.168.1.21:bb.git====dev1.4.x====front
'''

lines = data.split('\n')  # 按行分割字符串

dir=""

for line in lines:
    fields = line.split('====')  # 按 | 分割字段
    if len(fields)>2:
        if fields[3]=="service":
            cmd="git clone -b "+fields[2]+" http://yangzq:access@192.168.1.21:8082/"+fields[1].replace("git@192.168.1.21:","")
            print(cmd)
            dir+=",\"yyy/"+fields[0]+"\""

print(dir)