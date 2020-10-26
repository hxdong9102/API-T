#**************************************************************
# 文献系统view查询接口测试脚本v4.0
# url: http://129.211.129.101:9008/napi/v1/article/view?id=1
# Author: Dong Haixia
# Date: 2020-10-21
#**************************************************************

# 导入类库
import requests
import json
import csv

# 从csv文件中读取参数
with open("api_002_param.csv", 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    for row in rows:
        #print(row[0], row[1], row[2])

        url = "http://129.211.129.101:9008/napi/v1/article/view?id="+row[0]
        # 发送请求
        response = requests.get(url).text
        # print(response)
        # 把响应内容转换为字典格式,提取id
        if row[1] == 'Y':
            result = json.loads(response)['id']
            # print(result)
            # print(type(result))
        else:
            result = json.loads(response)['status']


        # 测试
        if result == int(row[2]):
            print("API testing passed.")
        else:
            print("API testing not passed.")