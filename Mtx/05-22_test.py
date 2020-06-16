# while True:
#     work_year = input('请输入您的工作年限：')
#     if work_year.isdigit():
#         new_work_year = int(work_year)
#         if new_work_year >= 8:
#             print('高级测试工程师')
#         elif new_work_year < 8 and new_work_year >= 3:
#             print('中级测试工程师')
#         elif new_work_year < 3:
#             print('初级测试工程师')
#     else:
#         print('您输入的年限有误')
#         break
# my_data = open('D:\order.txt','a+',encoding='utf8')
# city = ['beijing','shanghai','guangzhou']
# for line in my_data.readlines(city):
#     print(line)
# r_data = my_data.read()
# print(r_data)
# 写入20行数据
# a=0
# while a < 20:
#     w_data = my_data.write('Hello,world,chdongy!\n')
#     print(w_data)
#     a+=1;
# my_data.close()

# my_data = open('D:\order.txt','r',encoding='utf8')
# readlines一次读取所有内容 和read类似
# for line in my_data.readlines():
#     print(line.strip(),type(line))
# my_data.close()


# 通过Open函数实现文件的备份
r_pic = open(r'D:\微信图片_20200402220028.jpg','rb')
w_pic = open(r'D:\微信图片_20200402220028_bak1.jpg','wb')
r = r_pic.read()
w_pic.write(r)
r_pic.close()
w_pic.close()