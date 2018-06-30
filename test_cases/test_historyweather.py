#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 15:51  
# @Author  : longbolee  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_historyweather.py
# @Software: PyCharm

import requests
from config import config
import unittest


class testHistoryWeather(unittest.TestCase):
    def setUp(self):
        self.key = config.appkey
        self.province_url = config.host + "province"
        self.city_url = config.host + "citys"
        self.westher_url = config.host + "weather"
        pass

    def tearDown(self):
        pass


    #测试获取省份列表接口
    def test_get_provincelist(self):
        param = "key=" + self.key
        res = requests.set(self.province_url, param)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason") ,"查询成功")
        pass

    # 测试获取城市列表接口
    def test_get_citylist(self):
        payload = {"key":self.key,"province_id":1}
        res = requests.post(self.city_url, data=payload)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason"),"查询成功")
        pass

    # 测试获取省份列表接口
    def test_get_historyweather(self):
        payload = {"key":self.key, "city_id":1, "weather_date":"2018-06-01"}
        res = requests.post(self.westher_url, data=payload)
        jsonRes = res.json()
        pass


    if __name__ = "__main__":
        unittest
