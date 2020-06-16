# coding:utf-8
import requests
# HTTP各种接口
# 1、无参数的get请求
# res = requests.get(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince')
# print('响应内容为:\n' + res.text,'\n响应状态码为:'+ str(res.status_code))
# 2、无参数的Post请求
# res = requests.post(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince')
# print('响应内容为:\n' + res.text,'\n响应状态码为:'+ str(res.status_code))
# 3、有参数的get请求
# params ={'theRegionCode':'3117'}
# res = requests.get(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString',params=params)
# print('响应内容为:\n' + res.text,'\n响应状态码为:'+ str(res.status_code))
# 4、post正文类型
#     1、urlencoded
# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
# data = {'theRegionCode':'3117'}
# headrs = {'Content-Type':'application/x-www-form-urlencoded'}
# res = requests.post(url=url,
#               data=data,
#               headers = headrs)
# print('响应状态码为:'+ str(res.status_code),'\n响应内容为:\n' + res.text)
    # 2、标准的form表单 formdata
    # form表单形式提交数据，不需要指定Content-Type
# data = {'username':'2018','email':'88990@qq.com','password':'asdfgh123456'}
# res = requests.post(url='http://139.139.132.220:9000/event/index/submit_info',data=data)
# print(res.text)
    #3、标准的form表单 value带有文件的二进制数据--文件
    # open():打开一个文件变成二进制流格式
# url = 'http://139.139.132.220:9000/event/index/uploadFile/'
# # data = {'myfile':open('D:\\demo.html','rb')}
# # res = requests.post(url=url,files=data)
# # print(res.text)

    #4、xml纯文本格式post请求 webservices接口 soap协议
# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx'
# data = '''<?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <getSupportCityString xmlns="http://WebXml.com.cn/">
#       <theRegionCode>3117</theRegionCode>
#     </getSupportCityString>
#   </soap:Body>
# </soap:Envelope>'''
# headers = {'Content-Type':'text/xml'}
# res = requests.post(url=url,data=data,headers=headers)
# print(res.text)
    #5、json纯文本格式post请求 webservices接口 soap协议
# url = 'http://139.199.132.220:9000/event/weather/getWeather/'
# data = '{"theCityCode": 1}' #是一串json格式的字符串
# headers = {'Content-Type':'application/json'}
# res = requests.post(url=url,data=data,headers=headers)
# print(res.text)
    #5-2、json纯文本格式post请求 webservices接口  data不为纯文本而是一个字典 传参时，入参不为data，而是json
# url = 'http://139.199.132.220:9000/event/weather/getWeather/'
# data = {"theCityCode": 1} #是一个字典
# headers = {'Content-Type':'application/json'}
# res = requests.post(url=url,json=data,headers=headers)
# print(res.text)

import base64
# 系统管理员登录接口
password = 'abchuicehuice!@#'
a = base64.b64encode(password.encode('utf-8'))
b = str(a,'utf-8')
url = 'http://139.199.132.220:9000/event/api/register/'
headers = {'Content-Type':'application/x-www-form-urlencoded'}
data = {'username':'huice','password':b}
result = requests.post(url=url,headers=headers,data=data)
print(result.text)




# num = [13,43,2,45,32,25,11]
# for i in range(len(num)-1):
#     for j in range(len(num)-1):
#         if num[j] > num[j+1]:
#             num[j],num[j+1] = num[j+1],num[j]
# print(num)
