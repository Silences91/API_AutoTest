import os

from locust import TaskSet, HttpUser, between, task


class MyKJsonTask(TaskSet):
    url = '/pinter/com/buy'
    def setup(self):
        print('任务初始化')
    def teardown(self):
        print('任务结束')
    def on_start(self):
        print('用户初始化')
    def on_stop(self):
        print('用户结束')
    @task
    def MyKJson(self):
        self.KJson_data = {'param':'{"skuId":123,"num":10}'}
        print(f'请求参数为：{self.KJson_data}')
        with self.client.post(url=self.url,json=self.KJson_data,name = 'KJson_Post接口',timeout = 10,catch_response = True) as response:
            res_dict = response.json()
            print(f'响应参数为：{res_dict}')
            if res_dict['message'] == 'success':
                response.success()
            else:
                response.failure(res_dict['message'])

class MyPost(HttpUser):
    tasks = [MyKJsonTask]
    host = 'http://localhost:8080'
    wait_time = between(2,3)

if __name__ == '__main__':
    os.system('locust -f Locust_KJson.py')
