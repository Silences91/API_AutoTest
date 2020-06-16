# -*- coding: utf-8 -*-
# @Author : DONGYAC
# @Time : 2020-05-29 下午 23:26
# @File : test.py
import requests
def upload_file():
    url = 'http://localhost:8080/pinter/file/api/upload2/'
    file_data = {'file':open(r'D:/北京社保参保凭证.pdf','rb')}
    res = requests.post(url=url,files = file_data)
    print(f'响应内容为：{res.json()}')
def download_file():
    url = 'http://localhost:8080/pinter/file/api/download'
    para = {'id':6}
    res = requests.get(url=url,params= para)
    res_len = len(res.content)
    print(f'响应内容为：{res_len}')
def write_file():
    # a = 0
    # while a < 10:
    #     with open('D:/aaa.txt','a') as w:
    #         w.write('Hello，wolrd！\n')
    #     a += 1
    # with open('D:/aaa.txt','r') as r:
    #     print(r.read())
    with open('D:/replay_pid13508.log','r') as m:
        print(m.read(5000))


if __name__ == '__main__':
    # upload_file()
    # download_file()
    write_file()

