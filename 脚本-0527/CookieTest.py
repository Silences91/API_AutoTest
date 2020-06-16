# -*- coding:utf-8 -*-
# Author : beihe
# Date : 2020/5/24 19:17
import os

from locust import TaskSet, task, HttpLocust, between, HttpUser


class MyCookieTask(TaskSet):
    login_url = '/pinter/bank/api/login'
    query_url = '/pinter/bank/api/query'

    def on_start(self):
        print('用户初始化')
        login_data = {'userName': 'admin', 'password': '1234'}
        print(f'登录请求的参数为：{login_data}')
        with self.client.post(self.login_url, data=login_data, name='银行登录接口', timeout=10,
                              catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            resp_dict = response.json()
            print(f'登录响应数据为：{resp_dict}')

    def on_stop(self):
        print('用户结束')

    @task
    def post_test(self):
        # 定义一个对象属性
        post_data = {'userName': 'admin', 'password': '1234'}
        query_data = {'userName': 'admin'}
        print(f'查询余额请求的参数为：{post_data}')
        with self.client.get(self.query_url, params=query_data, name='post-kv接口', timeout=10, catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            resp_dict = response.json()
            print(f'查询余额响应数据为：{resp_dict}')
            if resp_dict['message'] == 'success':
                # 请求成功
                response.success()
            else:
                # 请求失败
                response.failure(resp_dict['message'])


class MyCookieUser(HttpUser):
    tasks = [MyCookieTask]
    host = 'http://localhost:8080'
    wait_time = between(2, 2)


if __name__ == '__main__':
    os.system('locust -f CookieTest.py')
