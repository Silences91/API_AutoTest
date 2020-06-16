#-*- coding:utf-8 -*-
# Author : beihe
# Date : 2020/5/24 19:17
from locust import TaskSet, task, HttpLocust, between, HttpUser


class MyTask(TaskSet):

    def setup(self):
        print('任务初始化')

    def teardown(self):
        print('任务结束')

    def on_start(self):
        print('用户初始化')

    def on_stop(self):
        print('用户结束')

    @task
    def pinter_test(self):
        print('业务运行')


class MyUser(HttpUser):
    tasks = [MyTask]
    host = 'http://localhost:8080'
    wait_time = between(2,2)


    def setup(self):
        print('Locust初始化')


    def teardown(self):
        print('Locust结束')