#-*- coding:utf-8 -*-
# Author : beihe
# Date : 2020/5/24 19:17
import json
import os
import random
import uuid
from locust import TaskSet, task, between, HttpUser


class MyJsonTask(TaskSet):

    url = '/pinter/com/register'
    def on_start(self):
        print('用户初始化')

    def on_stop(self):
        print('用户结束')


    @task
    def json_test(self):
        # 定义一个对象属性
        self.json_str = '{"userName":"test","password":"1234","gender":1,"phoneNum":"110","email":"beihe@163.com","address":"Beijing"}'
        # 将json字符串转换为字典
        self.json_data = json.loads(self.json_str)
        phoneNum = random.randint(1000,9999)
        address = str(uuid.uuid1())
        self.json_data['phoneNum'] = phoneNum
        self.json_data['address'] = address
        print(f'请求的参数为：{self.json_data}')
        with self.client.post(self.url, json=self.json_data ,name='json接口', timeout=10, catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            resp_dict = response.json()
            print(f'响应数据为：{resp_dict}')
            if resp_dict['message'] == '注册成功':
                # 请求成功
                response.success()
            else:
                # 请求失败
                response.failure(resp_dict['message'])

class MyJsonUser(HttpUser):
    tasks = [MyJsonTask]
    host = 'http://192.168.31.113:8080'
    wait_time = between(0,0)


if __name__ == '__main__':
    os.system('locust -f JsonTest.py')