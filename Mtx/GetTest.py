# -*- coding:utf-8 -*-
# Author : beihe
# Date : 2020/5/24 19:17
import os

from locust import TaskSet, task, between, HttpUser
from locust.contrib.fasthttp import FastHttpUser


class MyGetTask(TaskSet):
    url = '/pinter/com/getSku'

    def on_start(self):
        print('用户初始化')

    def on_stop(self):
        print('用户结束')

    @task
    def get_test(self):
        # 定义一个对象属性
        self.query_data = {'id': 1}
        print(f'请求的参数为：{self.query_data}')
        with self.client.get(self.url, params=self.query_data, name='get接口', timeout=10, catch_response=True) as response:
            # 接受接口返回值中的响应文本
            resp_str = response.text
            print(f'响应数据为：{resp_str}')
            if 'success' in resp_str:
                # 请求成功
                response.success()
            else:
                # 请求失败
                response.failure(resp_str)


class MyGetUser(HttpUser):
    tasks = [MyGetTask]
    host = 'http://localhost:8080'
    wait_time = between(2, 2)


if __name__ == '__main__':
    os.system('locust -f GetTest.py')
