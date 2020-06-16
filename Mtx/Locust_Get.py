import os

from locust import between, task, HttpUser, TaskSet


class MyGetTask(TaskSet):
    url = '/pinter/com/getSku'
    # def setup(self):
    #     print('任务初始化')
    # def teardown(self):
    #     print('任务结束')
    def on_start(self):
        print('用户初始化')
    def on_stop(self):
        print('用户结束')
    @task
    def Myget(self):
        self.query_data = {'id':1}
        print(f'请求参数为:{self.query_data}')
        with self.client.get(self.url,params = self.query_data,name = 'Get接口',timeout = 10,catch_response=True) as res:
            # 将接口返回值中的json提取出来，转换为一个字典
            res_dict = res.json()
            print(f'响应数据为:{res_dict}')
            if res_dict['message'] == 'success':
                # 请求成功
                res.success()
            else:
                # 请求失败
                res.failure(res_dict['message'])


class MyGet(HttpUser):
    tasks = [MyGetTask]
    host = 'http://localhost:8080'
    wait_time = between(2,5)

if __name__ == '__main__':
    os.system('locust -f Locust_Get.py')