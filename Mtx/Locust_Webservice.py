# -*- coding: utf-8 -*-
# @Author : DONGYAC
# @Time : 2020-05-31 下午 15:22
# @File : Locust_Webservice.py

import json
import os
import random
from locust import TaskSet, task, between, HttpUser


class MyWebserviceTask(TaskSet):

    url = '/WebServices/MobileCodeWS.asmx?op=getMobileCodeInfo'
    header = {'Content-Type': 'text/xml; charset=utf-8'}
    def on_start(self):
        print('用户初始化')

    def on_stop(self):
        print('用户结束')


    @task
    def Webservice_test(self):
        phoneNum = '185' + str(random.randint(10000000, 99999999))
        # 定义一个对象属性
        self.ws_str =f'<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><getMobileCodeInfo xmlns="http://WebXml.com.cn/"><mobileCode>{phoneNum}</mobileCode><userID></userID></getMobileCodeInfo></soap:Body></soap:Envelope>'
        print(f'电话号码为：{phoneNum}')
        with self.client.post(self.url, headers = self.header,data=self.ws_str ,name='webservice接口', timeout=10, catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            resp_text = response.text
            print(f'响应数据为：{resp_text}')
            if phoneNum in resp_text:
                # 请求成功
                response.success()
            else:
                # 请求失败
                response.failure(resp_text)

class MyWebseriveUser(HttpUser):
    tasks = [MyWebserviceTask]
    host = 'http://ws.webxml.com.cn'
    wait_time = between(2,2)


if __name__ == '__main__':
    os.system('locust -f Locust_Webservice.py')