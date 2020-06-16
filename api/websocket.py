# -*- coding:utf8 -*-

import threading
import hashlib
import socket
import base64
import json
global clients
clients = {}

city = {'哈尔滨': '116',  '长春': '650', '沈阳': '726'}

weather = { '116': '气温：24℃；风向/风力：东南风 1级；湿度：82%',
            '650': '气温：24℃；风向/风力：西南风 1级；湿度：91%',
            '726': '气温：27℃；风向/风力：南风 4级；湿度：83%'
           }

# 通知客户端
def notify(message):
    for connection in clients.values():
        connection.send('%c%c%s' % (0x81, len(message), message))


# 客户端处理线程
class websocket_thread(threading.Thread):
    def __init__(self, connection, username):
        super(websocket_thread, self).__init__()
        self.connection = connection
        self.username = username

    def run(self):
        print ('new websocket client joined!')
        data = self.connection.recv(1024)
        headers = self.parse_headers(data)
        token = self.generate_token(headers['Sec-WebSocket-Key'])
        self.connection.send('\
HTTP/1.1 101 WebSocket Protocol Hybi-10\r\n\
Upgrade: WebSocket\r\n\
Connection: Upgrade\r\n\
Sec-WebSocket-Accept: %s\r\n\r\n' % token)
        while True:
            try:
                data = self.connection.recv(1024)
            except socket.error as e:
                print ("unexpected error: "), e
                clients.pop(self.username)
                break
            data = self.parse_data(data)
            if len(data) == 0:
                continue
            try:
                data = json.loads(data)
            except:
                message = json.dumps({'msg': '请求参数格式错误'}, ensure_ascii=False)
            else:
                data = data.get('question')
                if data:
                    if data == '查询城市':
                        message = json.dumps(city, ensure_ascii=False)
                    elif data.isdigit():
                        info = weather.get(data)
                        if info:
                            message = json.dumps({'msg': info}, ensure_ascii=False)
                        else:
                            message = json.dumps({'msg': '您所在的城市尚未开通此服务'}, ensure_ascii=False)
                    else:
                        message = json.dumps({'msg': '暂时支持的问题是：【查询城市】 【城市id】'}, ensure_ascii=False)
                else:
                    message = json.dumps({'msg': '请求参数question不存在'}, ensure_ascii=False)
            notify(message)

    def parse_data(self, msg):
        v = ord(msg[1]) & 0x7f
        if v == 0x7e:
            p = 4
        elif v == 0x7f:
            p = 10
        else:
            p = 2
        mask = msg[p:p + 4]
        data = msg[p + 4:]
        return ''.join([chr(ord(v) ^ ord(mask[k % 4])) for k, v in enumerate(data)])

    def parse_headers(self, msg):
        headers = {}
        header, data = msg.split('\r\n\r\n', 1)
        for line in header.split('\r\n')[1:]:
            key, value = line.split(': ', 1)
            headers[key] = value
        headers['data'] = data
        return headers

    def generate_token(self, msg):
        key = msg + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        ser_key = hashlib.sha1(key).digest()
        return base64.b64encode(ser_key)


# 服务端
class websocket_server(threading.Thread):
    def __init__(self, port):
        super(websocket_server, self).__init__()
        self.port = port

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', self.port))
        sock.listen(5)
        print ('websocket server started!')
        while True:
            connection, address = sock.accept()
            try:
                username = "ID" + str(address[1])
                thread = websocket_thread(connection, username)
                thread.start()
                clients[username] = connection
            except socket.timeout:
                print ('websocket connection timeout!')


if __name__ == '__main__':
    server = websocket_server(6080)
    server.start()