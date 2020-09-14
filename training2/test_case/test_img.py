# ***************************************************************
# Author: Dong Haixia
# Date: 2020-7-10
# Description: 提取去图片中的文字，测试提取结果的正确性。
# Dataset: ../test_data/img_data.xlsx
# ***************************************************************


import requests
import pytest
# 数据驱动 -- 百度ai 接口自动化测试
# 处理参数  -- access_token
# 数据导入


def get_token():
    """
    获取access_token
    :return:
    """
    # 获取token的请求地址
    get_url = "https://aip.baidubce.com/oauth/2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": "hvOaGIRHgWHbDM3McW9o9obp",
        "client_secret": "wNsVW8TkbPVVwQKsYdPkjGf9XiSLu6HS"
    }
    # 发送请求
    res = requests.post(url=get_url, data=data)
    # 处理响应 json  对数据进行处理  json--dict
    token_data = res.json()["access_token"]
    return token_data


# 导入数据集
from test_data import img_data

# 获取Sheet中的图片信息
img_info =img_data.get_img_imfo()

@pytest.mark.parametrize("img_url,exp_words", img_info)

def test_01(img_url,exp_words):

    data = {
        "access_token": get_token(),
        "url": img_url
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basichttps://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    res = requests.post(url=url, data=data, headers=headers)
    # json  -- 对拿到的数据转换
    # 只需要展示单词  dict
    words = res.json()["words_result"]
    
    img_str = ""
    for i in words:
        img_str += i["words"]
    assert img_str == exp_words
