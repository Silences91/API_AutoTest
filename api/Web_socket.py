# coding: utf-8
import time
import websocket
from websocket import create_connection
ws = websocket.create_connection(url = 'ws://127.0.0.1:6080')
ws.send('{"question":"116"}')
print(ws.recv())
# while True:  # 一直链接，直到连接上就退出循环
#     time.sleep(2)
#     try:
#         ws = create_connection(url)
#         print(ws)
#         break
#     except Exception as e:
#         print('连接异常：', e)
#         continue
# while True:  # 连接上，退出第一个循环之后，此循环用于一直获取数据
#     ws.send('{"question":"116"}')
#     response = ws.recv()
