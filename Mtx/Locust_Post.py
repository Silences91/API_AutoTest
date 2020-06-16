import os

from locust import TaskSet, HttpUser, between, task


class MyPostTask(TaskSet):
    url = '/pinter/com/login'
    # def setup(self):
    #     print('任务初始化')
    # def teardown(self):
    #     print('任务结束')
    def on_start(self):
        print('用户初始化')
    def on_stop(self):
        print('用户结束')
    @task
    def MyPost(self):
        self.post_data = {'userName':'admin','password':'1234'}
        print(f'请求参数为：{self.post_data}')
        with self.client.post(url=self.url,data=self.post_data,name = 'kv_Post接口',timeout=10,catch_response = True) as res:
            res_str = res.text
            print(f'响应数据为:{res_str}')
            if 'success' in res_str:
                res.success()
            else:
                res.failure(res_str)

class MyPost(HttpUser):
    tasks = [MyPostTask]
    host = 'http://localhost:8080'
    wait_time = between(2,2)

if __name__ == '__main__':
    os.system('locust -f Locust_Post.py')