import json
import os
import random
import uuid

from locust import TaskSet, HttpUser, between, task


class MyJsonTask(TaskSet):
    url = '/pinter/com/register'
    # def setup(self):
    #     print('任务初始化')
    # def teardown(self):
    #     print('任务结束')
    def on_start(self):
        print('用户初始化')
    def on_stop(self):
        print('用户结束')
    @task
    def MyJson(self):
        # self.headers = {'Content-Type':'application/json'}
        self.json_str = '{"userName":"test","password":"1234","gender":1,"phoneNum":"110","email":"beihe@163.com","address":"Beijing"}'
        self.json_data = json.loads(self.json_str)
        phoneNum = '139'+ str(random.randint(10000000,99999999))
        address = str(uuid.uuid1())
        self.json_data['phoneNum'] = phoneNum
        self.json_data['address'] = address
        print(f'请求参数为：{self.json_data}')
        with self.client.post(url=self.url,json=self.json_data,name = 'Json_Post接口',timeout=10,catch_response = True) as res:
            # 将接口返回值中的json提取出来，转换为一个字典
            res_dict = res.json()
            print(f'响应数据为:{res_dict}')
            if res_dict['message'] == '注册成功':
                res.success()
            else:
                res.failure(res_dict['message'])

class MyPost(HttpUser):
    tasks = [MyJsonTask]
    host = 'http://localhost:8080'
    wait_time = between(2,2)

if __name__ == '__main__':
    os.system('locust -f Locust_Json.py')