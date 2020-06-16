#-*- coding:utf-8 -*-
# Author : beihe
# Date : 2020/5/24 19:17
import hashlib
import json
import os
import random
import time
import uuid
from locust import TaskSet, task, between, HttpUser


class MySignTask(TaskSet):

    url = '/pinter/com/userInfo'

    def on_start(self):
        print('用户初始化')

    def on_stop(self):
        print('用户结束')


    @task
    def sign_test(self):
        # 定义一个对象属性
        self.json_str = '{"phoneNum":"123434","optCode":"testfan","timestamp":"12112121212","sign":"your sign data"}'
        # 将json字符串转换为字典
        self.json_data = json.loads(self.json_str)
        phoneNum = random.randint(1000,9999)
        my_time = int(time.time() * 1000)
        concat_data = f'{phoneNum}testfan{my_time}'
        # 对拼接后的数据加密
        sign_data = self.get_md5(concat_data)
        self.json_data['phoneNum'] = phoneNum
        self.json_data['timestamp'] = my_time
        self.json_data['sign'] = sign_data

        print(f'请求的参数为：{self.json_data}')
        with self.client.post(self.url, json=self.json_data ,name='sign接口', timeout=10, catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            resp_dict = response.json()
            print(f'响应数据为：{resp_dict}')
            if resp_dict['message'] == 'success':
                # 请求成功
                response.success()
            else:
                # 请求失败
                response.failure(resp_dict['message'])

    # md5加密
    def get_md5(self, data):
        md5 = hashlib.md5()
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()


class MySignUser(HttpUser):
    tasks = [MySignTask]
    host = 'http://localhost:8080'
    wait_time = between(2,2)


if __name__ == '__main__':
    os.system('locust -f SignTest.py')