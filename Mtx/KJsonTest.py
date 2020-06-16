#-*- coding:utf-8 -*-
# Author : beihe
# Date : 2020/5/24 19:17
import os

from locust import TaskSet, task, HttpLocust, between, HttpUser


class MyKJsonTask(TaskSet):

    url = '/pinter/com/buy'
    def on_start(self):
        print('用户初始化')

    def on_stop(self):
        print('用户结束')


    @task
    def kjson_test(self):
        # 定义一个对象属性
        self.post_data = {'param': '{"skuId":123,"num":10}'}
        print(f'请求的参数为：{self.post_data}')
        response = self.client.post(self.url, data=self.post_data ,name='post-kjson接口', timeout=10, catch_response=True)
        # 将接口返回值中的json提取出来，转换为一个字典
        resp_dict = response.json()
        print(f'响应数据为：{resp_dict}')
        if resp_dict['message'] == 'success':
            # 请求成功
            response.success()
        else:
            # 请求失败
            response.failure(resp_dict['message'])

class MyKJsonUser(HttpUser):
    task_set = MyKJsonTask
    host = 'http://localhost:8080'
    wait_time = between(2,2)


if __name__ == '__main__':
    os.system('locust -f KJsonTest.py')