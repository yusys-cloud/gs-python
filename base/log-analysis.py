import json
import numpy as np

log_file = "/home/ubuntu/yzq/go-proxy/proxy-1.log"  # 日志文件路径
costs = []  # 存储所有的 CostMs 值

with open(log_file, "r") as file:
    for line in file:
        try:
            data = json.loads(line)  # 解析 JSON 数据
            if "CostMs" in data:
                cost = data["CostMs"]  # 提取 CostMs 值
                costs.append(cost)
                # print(data["CostMs"],data["time"],data["Remote"])
        except json.JSONDecodeError:
            # 忽略解析错误的行
            continue

if costs:
    avg_cost = np.mean(costs)
    min_cost = np.min(costs)
    max_cost = np.max(costs)
    median = np.median(costs)
    percentile_25 = np.percentile(costs, 25)
    percentile_75 = np.percentile(costs, 75)
    variance = np.var(costs)
    std_deviation = np.std(costs)
    
    print("Average CostMs:", avg_cost)
    print("Minimum CostMs:", min_cost)
    print("Maximum CostMs:", max_cost)
    print("Median CostMs:", median)
    print("25th Percentile CostMs:", percentile_25)
    print("75th Percentile CostMs:", percentile_75)
    print("Variance:", variance)
    print("Standard Deviation:", std_deviation)
     # 计算大于 5000 的占比
    count_greater_than_5000 = sum(cost > 5000 for cost in costs)

    percentage_greater_than_5000 = (count_greater_than_5000 / len(costs)) * 100
    print("Percentage of CostMs > 5000:", percentage_greater_than_5000)
    print("Total:",len(costs))
else:
    print("No data found in the log file.")