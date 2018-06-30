#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 16:23  
# @Author  : longbolee  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : run.py  
# @Software: PyCharm

import  unittest
from test_suits import ranzhi_suite
from lib.HTMLTestRunner import HTMLTestRunner
import time

if __name__ == "__main__":
    suit = ranzhi_suite.get_suite()
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    with open('reports/{}',format())as report: