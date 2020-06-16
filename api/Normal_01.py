import unittest
import requests
from api.CheckPoint import CheckPoint
class Normal_01(unittest.TestCase):
    '''通用接口练习'''
    def setUp(self):
        self.url1 = 'http://localhost:8080/pinter/com/getSku'
        self.url2 = 'http://localhost:8080/pinter/com/login'
        self.url3 = 'http://localhost:8080/pinter/com/register'
        self.url4 = 'http://localhost:8080/pinter/com/buy'
        self.headers = {'Content-Type':'application/json'}
        self.check = CheckPoint() #实例化一个对象

    def tearDown(self):
        self.check.result() #判断用例状态

    def test_normal_01(self):
        '''带参数的get请求'''
        params = {'id': '1'}
        res = requests.get(url=self.url1,params=params)
        self.check.equal(res.status_code, 200)
        self.check.equal(res.json().get('message'), 'success')#接口返回json字符串，用res.json()可以将字符串转成字典的形式方便取值
        self.check.less_then(int(round(res.elapsed.total_seconds() * 1000)), 200)
    def test_normal_02(self):
        '''参数为k=v的POST接口'''
        data = {'userName':'admin','password':'1234'}
        res = requests.post(url=self.url2, data = data)
        self.check.equal(res.status_code, 200)
        self.check.equal(res.json().get('message'), 'success')
        self.check.less_then(int(round(res.elapsed.total_seconds() * 1000)), 200)
    def test_normal_03(self):
        '''参数为json的POST接口'''
        data = {"userName":"test","password":"1234","gender":1,"phoneNum":"110","email":"beihe@163.com","address":"Beijing"}
        res = requests.post(url=self.url3, headers = self.headers,json=data)
        self.check.equal(res.status_code,200)
        self.check.equal(res.json().get('code'),'0')
        self.check.less_then(int(round(res.elapsed.total_seconds() * 1000)),200)
    def test_normal_04(self):
        '''参数为k=json的POST接口'''
        data ={"skuId":123,"num":10}
        res = requests.post(url=self.url4, headers = self.headers,json=data)
        self.check.equal(res.status_code, 200)
        self.check.equal(res.json().get('code'), '0')
        self.check.less_then(int(round(res.elapsed.total_seconds() * 1000)), 200)