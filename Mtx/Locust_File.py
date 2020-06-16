# -*- coding: utf-8 -*-
# @Author : DONGYAC
# @Time : 2020-05-29 下午 20:50
# @File : Locust_File.py
# coding:utf-8
import os

from locust import task, between, HttpUser, SequentialTaskSet, TaskSet


class MyFileTask(TaskSet):
    url = '/pinter/file/api/upload2'
    url2 = '/pinter/file/api/download'
    def on_start(self):
        print('用户初始化')

    def on_stop(self):
        print('用户结束')


    @task(2)
    def upload_test(self):
        # 定义一个对象属性
        upload_data = {'file': open(r'D:\北京社保参保凭证.pdf','rb')}
        with self.client.post(self.url, files=upload_data ,name='文件上传接口', timeout=10, catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            # res_text = response.text
            # # print(f'请求url为：{self.url}')
            # print(f'响应数据为:{res_text}')
            #
            # if '上传成功' in res_text:
            #     response.success()
            # else:
            #     response.failure(res_text)
            res_text = response.json()
            print(f'响应数据为:{res_text}')
            if res_text['message'] == '上传成功':
                response.success()
            else:
                response.failure(res_text['message'])
    @task(1)
    def download_test(self):
        # 定义一个对象属性
        down_data = {'id':1}
        with self.client.get(self.url2, params = down_data, name='文件下载接口', timeout=10, catch_response=True) as response:
            # 将接口返回值中的json提取出来，转换为一个字典
            file_size = len(response.content)
            print(f'服务器返回body大小为:{file_size}')

            if file_size == 415521:
                response.success()
            else:
                response.failure('下载失败')


class MyUploadUser(HttpUser):
    tasks = [MyFileTask]
    host = 'http://localhost:8080'
    wait_time = between(2,2)


if __name__ == '__main__':
    os.system('locust -f Locust_File.py')