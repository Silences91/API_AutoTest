#-*- coding:utf-8 -*-
# Author : beihe
# Date : 2020/5/24 19:17
import json
import os
import queue
import random
import uuid
from locust import TaskSet, task, between, HttpUser


class MyParamTask(TaskSet):

    url = '/pinter/com/register'

    def on_start(self):
        # 获取自定义数据源的长度
        self.list_size = len(self.user.username_list)
        # 定义初始序号，默认=列表长度
        self.num = self.list_size
        print('用户初始化')

    def on_stop(self):
        print('用户结束')


    # @task
    def json_test(self):
        # 定义一个对象属性
        self.json_str = '{"userName":"test","password":"1234","gender":1,"phoneNum":"110","email":"beihe@163.com","address":"Beijing"}'
        # 将json字符串转换为字典
        self.json_data = json.loads(self.json_str)
        # 根据长度生成一个随机索引
        random_index = random.randint(0, self.list_size-1)
        # 获取列表中的随机索引值，并更新到字典里
        self.json_data['userName'] = self.user.username_list[random_index]

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


    # @task
    def json_test2(self):
        # 定义一个对象属性
        self.json_str = '{"userName":"test","password":"1234","gender":1,"phoneNum":"110","email":"beihe@163.com","address":"Beijing"}'
        # 将json字符串转换为字典
        self.json_data = json.loads(self.json_str)
        seq_index = self.num % self.list_size
        self.json_data['userName'] = self.user.username_list[seq_index]
        self.num += 1
        print(f'请求的参数为：{self.json_data}')
        with self.client.post(self.url, json=self.json_data, name='json接口', timeout=10,
                              catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            resp_dict = response.json()
            print(f'响应数据为：{resp_dict}')
            if resp_dict['message'] == '注册成功':
                # 请求成功
                response.success()
            else:
                # 请求失败
                response.failure(resp_dict['message'])

    # @task
    def json_test3(self):
        # 定义一个对象属性
        self.json_str = '{"userName":"test","password":"1234","gender":1,"phoneNum":"110","email":"beihe@163.com","address":"Beijing"}'
        # 将json字符串转换为字典
        self.json_data = json.loads(self.json_str)

        # 从队列里面取值，从头部获取一个值
        try:
            self.my_username = self.user.queue_data.get()
        except queue.Empty:
            print('队列中没有数据了')
            # 队列中的数据取完后，程序停止，不再运行
            exit(1)

        self.json_data['userName'] = self.my_username
        print(f'请求的参数为：{self.json_data}')
        with self.client.post(self.url, json=self.json_data, name='json接口', timeout=10,
                              catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            resp_dict = response.json()
            print(f'响应数据为：{resp_dict}')
            if resp_dict['message'] == '注册成功':
                # 请求成功
                response.success()
            else:
                # 请求失败
                response.failure(resp_dict['message'])

    @task
    def json_test4(self):
        # 定义一个对象属性
        self.json_str = '{"userName":"test","password":"1234","gender":1,"phoneNum":"110","email":"beihe@163.com","address":"Beijing"}'
        # 将json字符串转换为字典
        self.json_data = json.loads(self.json_str)

        # 从队列里面取值，从头部获取一个值
        try:
            self.my_username = self.user.queue_data2.get(block=False)#添加block参数-变为非阻塞式 输出Empty中的内容
        except queue.Empty:
            print('队列中没有数据了')
            # 队列中的数据取完后，程序停止，不再运行
            exit(1)

        self.json_data['userName'] = self.my_username
        print(f'请求的参数为：{self.json_data}')
        with self.client.post(self.url, json=self.json_data, name='json接口', timeout=10,
                              catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            resp_dict = response.json()
            print(f'响应数据为：{resp_dict}')
            if resp_dict['message'] == '注册成功':
                # 请求成功
                response.success()
            else:
                # 请求失败
                response.failure(resp_dict['message'])


class MyParamUser(HttpUser):
    tasks = [MyParamTask]
    host = 'http://localhost:8080'
    wait_time = between(2,2)

    # 定义一个数据列表
    username_list = []
    for i in range(1000):
        username_list.append('testfan_%d' % i)

    # 定义一个队列
    queue_data = queue.Queue()
    for i in range(10):
        queue_data.put_nowait('testfan_%d' % i)

    # 从文件读取数据到一个列表中
    queue_data2 = queue.Queue()
    with open('D:/order.txt','r') as f:
        for line in f.readlines():
            queue_data2.put_nowait(line.strip())

if __name__ == '__main__':
    os.system('locust -f ParamTest.py')