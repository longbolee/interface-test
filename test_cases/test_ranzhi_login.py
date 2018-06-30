#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 14:38  
# @Author  : longbolee  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_ranzhi_login.py.py
# @Software: PyCharm

import requests
import hashlib
import re
import unittest

class testRanzhiLonin(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1/ranzhi/www/sys/user-login-L3JhbnpoaS93d3cvc3lzLw==.html"
        self.username = "admin"
        self.password = "1234"
        pass

    def tearDown(self):
        pass

    def test_ranzhi_login(self):
        #1.请求登录页
        res = requests.get(self.url)
        #2.通过正则表达式获取v.random的值
        pattern = "(?=v.random = \").*(?=;<)"
        result = re.search(pattern, res.text).group()
        random_str = result.replace('v.random ="', '').replace('"' ,'')
        #3.对password进行加密
        step1 = hashlib.md5(random_str.encode('utf-8'))hexdigtext()
        tempstr = step1 + self.username
        step2 = hashlib
        newpassword = hashlib.md5(hashlib.md5(hashlib.md5(random_str.encode())))
        #4.构造请求参数
        payload = {"account":self.username,"password":}
        #5.发送请求
        pass

if ___name__ == "__main__":
    unittest