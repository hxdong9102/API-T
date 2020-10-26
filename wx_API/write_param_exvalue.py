#**************************************************************
# 文献系统view查询接口数据生成脚本v4.0
# Des: 把参数id和期待的返回值写入csv文件中
# Author: Dong Haixia
# Date: 2020-10-21
#**************************************************************


import csv

file = open("api_002_param.csv", "w", newline="")

for i in range(1, 10):
    if i in [3, 5, 9]:
        fwrite = csv.writer(file)
        fwrite.writerow([i, 'N', 404])
    else:
        fwrite = csv.writer(file)
        fwrite.writerow([i, 'Y', i])
file.close()