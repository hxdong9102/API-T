# ***************************************************************
# Author: Dong Haixia
# Date: 2020-7-25
# Description: 利用接口对图片进行锐化操作，将锐化后的图片保存。
# Request method: http-post
# ***************************************************************


import requests
import base64


def get_access_token():
    # 获取token的API
    url = "https://aip.baidubce.com/oauth/2.0/token"
    # 获取access-token需要的参数
    params = {
        "grant_type": "client_credentials",
        "client_id": "EbycoHo6kE28B8c9XDKERhGD",
        "client_secret": "owuXpBCH1WdqlNm8zt5jCdQG5pXSlhRk"
        }
    # 发送请求，获取响应数据
    response = requests.post(url, params)
    return response.json()['access_token']


def img_info(path):
    with open(path, 'rb') as f:
        img = base64.b64encode(f.read())
    return img


def processed_img(b64code, newpath):
    temp = base64.b64decode(b64code)
    with open(newpath, 'wb') as fp:
        fp.write(temp)
    return fp


data = {
    "access_token": get_access_token(),
    "image": img_info(r"D:\Learning-File\API_TEST\course\training1\2.JPG")
}
headers = {
    "Content_Type": "application/x-www-form-urlencoded"
    }
url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"

res = requests.post(url=url, data=data, headers=headers)
#print(res.text)
#print(res.json()['log_id'])
# b64code原图片被接口处理后的base64编码
b64code = res.json()['image']
newpath = r"D:\Learning-File\API_TEST\course\training1\3.JPG"
# 把处理后的图片保存到newpath
new_pic = processed_img(b64code, newpath)