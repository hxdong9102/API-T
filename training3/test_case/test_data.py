# ***************************************************************
# Author: Dong Haixia
# Date: 2020-7-25
# Description: 测试excel表格中计算结果的正确性，生成测试报告。
# Dataset: ../test_data/dataset.xlsx
# ***************************************************************


import pytest
from test_data import get_data


data = get_data.get_data_info()

def add (x, y):
    return x + y


# 参数化
@pytest.mark.parametrize("x,y,z", data)
def test_add(x,y,z):
    assert add(x, y) == z