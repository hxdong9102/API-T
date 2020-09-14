# ***************************************************************
# Author: Dong Haixia
# Date: 2020-7-10
# 针对文献管理系统中的文章阅读接口进行正常测试
# 接口说明：http://129.211.129.101:9003/napi/v1/article/view?id=1
# ***************************************************************


# 导入类库
import requests
import json
import pymysql


# 打开数据库连接
db = pymysql.connect('129.211.129.101', 'apitest', '51testing', 'mldigidoc', port=9004, charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 发送接口请求
id = 5
id_normal = [1, 2, 4, 6, 7, 8]
response = requests.get('http://129.211.129.101:9003/napi/v1/article/view?id=' + str(id)).text
#print(response)
#print(type(response))


# 提取接口验证点
result = json.loads(response)
#print(type(result))
if id in id_normal:
    result_id = result['id']

    # 使用execute方法执行SQL语句
    sql_cmd = "SELECT title FROM `article` WHERE id=" + str(id)
    cursor.execute(sql_cmd)
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()
    #print(data)
    #print(type(data))
    print(data[0])
    print(result['title'])

    # 进行验证点验证-正常字段
    if result_id == id and data[0] == result['title']:
        print("正常测试通过")
    else:
        print("正常测试失败")
else:
    result_status = result['status']

    # 进行验证点验证-异常字段
    if result_status == 404:
        print("异常测试通过")
    else:
        print("异常测试失败")


# 关闭数据库连接
db.close()