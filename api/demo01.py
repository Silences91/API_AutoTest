# -*- coding:utf8 -*-
# print('Bob said\nI\'m OK.')
# print('''Bob said
# I'm OK.''')
# print('''div[@id='goodItem']/a''')
# print(r"div[@id='goodItem']/a")
# print('''Bob said "I'm OK".''')
# # print('\nC:\Program Files\\fnord\\foo\\bar\\baz\\frozz\n^test/\d{n,}/$')
# print('''\n
# C:\Program Files\fnord\foo\bar\baz\frozz
# ^test/\d{n,}/$ ''')

# a =-11
# b =3
# print(a// b)
# print(a % b)
#
# e = [1,3,5,3,9,5]
# f =[]
# f=e.append(8)
# print(f)
#
# name = 'chensir'
# ee = ['1','2','4','3']
# ec = [1,2,4]
# month = 2
# money = 23.23
# a = ("亲爱的%s您好，您%d月的话费为100元，余额为%.2f元。" % (name,month,money))
# print(a)
# print(len(name))
# print(name[-1])
# print(name[len(name)-1])
# print(name[-1])
# print('='.join(name))
# print(''.join(ee))
#
# str = '亲爱的{name}你好，您{month}月的话费为100元，余额为{money}元。'
# print(str.format(name=name,month=month,money=money))
#
# protocol = 'http'
# domain = '192.168.2.111'
# url = 'huice/event/api/add'
# data ="title=python大会&time=2018-01-06"


# str1 = '{protocol}//{domain}/{url}?{data}'
# str2=str1.format(protocol=protocol,domain=domain,url=url,data=data)
# print(str2)
# print(str2.replace('http','https'))
# http://192.168.2.111/huice/event/api/add?title=python大会&time=2018-01-06

# replace 函数
# t = 'hello world'
# print(t.replace('l','j',1)) # 可以追加参数-指定替换的次数
# print(t.count('l'))
# print(t.find('l',3,7))
# print(t.index('l'))
#
# source ='1,3,5,7,9'
# print(source.split(',')) #字符串切割  字符串转List
# print(len(source))
# print(source.find('7'))
#
# source=['1','3','4','5','6']
# print(','.join(source))   #列表List转字符串

# title=华为春季新品发布会&sign=0&limit=100&status=0&address=国家会议中心&time=2018-03-28
# message ='title=华为春季新品发布会&sign=0&limit=100&status=0&address=国家会议中心&time=2018-03-28'
# spl = message.split('&')
# print(spl)

# browser = 'fire fox'
# print(browser.capitalize())
# print(browser.strip())
# print(browser.replace(' ',''))


# 1.接受用户输入的一个字符串，如果是正整数就判断是否能同时被3和7整除
# score = input('请输入您的成绩：')
#
# if score.isdigit():
#     score = int(score)
#     if score >= 0:
#         if score % 3 == 0 and score % 7 == 0:
#             print('%d能同时被3和7整除' % score)
#         else:
#             print('%d不能同时被3和7整除 ' % score)
#     else:
#         print('输入的为非正整数')
# else:
#     print('您输入的为非数字！')

# 2.根据输入的月份来输出，这个月有几天(默认2月有28天，不考虑闰年)

# month = input('请输入月份：')
# if month.isdigit() :
#     month=int(month)
#     if  0 <= month <=12:
#         if month in (1,3,5,7,8,10,12):
#             print('%d月有31天！' % month)
#         elif month in (4,6,9,11):
#             print('%d月有30天！' % month)
#         elif month == 2:
#             print('%d月有28天！' % month)
#     else:
#         print('您输入的不是有效月份，请重新输入！')
# else:
#     print('您输入的月份有误，请重新输入！')

# 3.接收用户输入一个年份，判断是否是闰年(判断闰年的方法是该年能被4整除并且不能被100整除，或者是可以被400整除)

# year = input('请输入月份：')
# if year.isdigit():
#     year=int(year)
#     if year % 4 == 0 and year % 100 != 0:
#         print('%d年为闰年!' % year)
#     elif  year % 400 == 0:
#         print('%d年为闰年!' % year)
#     else:
#         print('%d年为平年!' % year)
#
# else:
#     print('您输入的不是有效月份！')

# 4.某电信公司的市内通话费计算标准如下：三分钟内0.2元，
# 			  三分钟后每增加一分钟增加0.1元，不足一分钟的按一分
# 			  钟计算。要求编写程序，给定一个通话时间（单位：秒）
# 			  计算出应收费金额。

# time = input('请输入通话时间:')
# total = 0.0
# if time.isdigit():
#     time = int(time)
#     if time < 180:
#         print('通话费用为0.2元!')
#     elif time == 180:
#         total = 0.2 + 0.1
#         print('通话费用为%.1f元!' % total)
#     else:
#         total = 0.2 + ((time - 180) // 60 * 0.1) + 0.1
#         print('通话费用为%.1f元!' % total)
# else:
#     print('您输入的时间格式有误！')

# 接收用户输入金额，当为正整数时，停止输入
# while True:
#     money = input('请输入您需要的金额：')
#     if money.isdigit():
#         money = int(money)
#         print(money)
#         break

# d = 0
# while d < 10:
#     c = input('请输入：')
#     c = int(c)
#     print(c)
#     d = d + 1

# a = [1,2,3,4,5,6]
# for i in a:
#     print(i)
#
# for j in range (0,len(a)):
#     print(a[j])





# b = ['2','4','5','8']
# a = ''.join(b)
# print(a)
# for i in b:
#     print(i)


# 0.输入n, 计算1到n的阶乘之和
# r = input('请输入一个整数：')
# if r.isdigit():
#     r = int(r)
#     total = 0
#     for i in range(1,r+1):
#         total = total + i
#     print(total)
# else:
#     print('您输入的为非整数！')

# 1.分别使用while与for循环输出1-100之间的所有偶数
# a = 1
# while a <= 100:
#     if a % 2 == 1:
#         print(a)
#     else:
#         pass
#     a = a + 1

# for i in range (1,101):
#     if i  % 2 == 1:
#         print(i)
# 用两行代码输出1-100之间的偶数
# for i in range(100,0,-2):
#     print(i)

# 3.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# str = input('请输入一串不包含汉字的字符：')
# # print(type(len(str)))
# a = 0
# b = 0
# c = 0
# d = 0
# for i in str:
#     if i.isdigit():
#         a = a + 1
#         # print(type(a))
#     elif i.isalpha():
#         b = b + 1
#     elif i.isspace():
#         c = c + 1
#     else:
#         d = d + 1
# print('您输入的字符中数字为:%d,字母为:%d,空格为:%d,其他字符为:%d.' % (a , b,c,d))


# 1.给定一个字符串 target = 'hello huice'，从中找出第一个不重复的字符,输出它是第几位
# target = 'hello huice'
# for j in target:
#     if target.count(j) == 1:
#         print(target.index(j))
#         break
# 2.去除上一题中的重复字符，得到一个新的字符串
# new_target =''
# for k in target:
#     if target.count(k) ==1:
#         new_target +=k
# print(new_target)

# 九九乘法表
def chengfa_99():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d X %d = %2d '% (j,i,i*j),end=' ')
        print('')
# 练习：员工工资表，查询结果集如下：((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
# 			  1.计算员工的平均工资
# 			  *2.输出工资最高的员工姓名
def lianxi1():
    salary = ((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
    s = 0
    for i in salary:
        s = s + i[2]
    avg = s / len(salary)
    print(int(avg))

    m = salary[0]
    for i in range(len(salary)):
        if salary[i][2] > m[2]:
            m = salary[i]
    print(m[1])
# if __name__ == '__main__':
#     lianxi1()
#     chengfa_99()

# str = 'chendy'
# print(str + '1314')
# k = [1,3,5,7,9]
# print(type(k))
# k[0:3]=[1,3,5,7,9]
# n = []
# for i in k:
#     i = i + 1
#     n.append(i)
# print(n)
# d = ['1','2','4','5']
# d.append('学生')
# print(d)
# d.pop()
# print(d)
# d.insert(1,'7')
# print(d)
# del d[:2]
# print(d)
# d.remove('4')
# print(d)
# d[:] = ['麻花','狗不理包子']
# print(d)

# group = {'师父':'唐三藏', '大师兄':'孙行者', '二师兄':'猪八戒', '沙师弟':'沙和尚'}
# print(group['沙师弟'])
# group['白龙马'] = '敖烈'
# print(type(group.keys()))
# print(list(group.keys()))
# print(group.values())
# print(group.items())
# for i,j in group.items():
#     print(i,j)

# def add(x,y):
#     a = 0
#     for i in range(x,y):
#         a+= i
#     print(a)
#     return a
# add(1,10)

# 三元表达式 - 条件为真时的结果 if 条件表达式  else 条件为假时的结果
# print('y' if 5>3 else 'x')

# 用户输入一个数字判断该数能否被3整除
# number = input('请输入一个数字：')
# if number.isdigit():
#     number=int(number)
#     if number % 3 == 0:
#         print('%2d能被3整除！' % number)
#     else:
#         print('%2d不能被3整除！' % number)
# else:
#     print('您输入的数字不合法！')

# 阶乘  1~3= 1*2*3 = 6
# result = 1
# for i in range(10):
#     i += 1
#     result *= i
# print(result)

# 接收输入数字，直到为9999时，停止接收输入。
# while True:
#     a = input('请输入：')
#     if a.isdigit():
#         a = int(a)
#         if a==9999:
#             break
#         else:
#             print(a)
#     else:
#         print('您输入的数据不合法！')
# enumerate-可同时取下标和元素
# zk = ['张三','李四','王五']
# for i,j in enumerate(zk):
#     print(j,i)
# 系统随机生成一个随机数，猜数字
# import random
# rand_int = random.randint(1,1024)
# print(rand_int)
# while True:
#     num = input('请输入一个数字：')
#     if num.isdigit():
#         num=int(num)
#         if num > rand_int:
#             print('对不起，您猜的数字太大了！')
#         elif num < rand_int:
#             print('对不起，您猜的数字太小了！')
#         else:
#             print('恭喜你，猜对了！')
#             break
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# def is_palindrome(n):
#     a = str(n)
#     b = int(a[::-1])
#     a = int(a)
#     if a == b:
#         print(f'{a}是回文数！',type(a))
#     else:
#         print(f'{a}不是回文数！',type(a))
# is_palindrome(123454321)
# 打印出100-999中所有的"水仙花数"，所谓"水仙花数"是指一
# 个三位数，其各位数字立方和等于该数本身。例如：
# 153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
# for i in range(100,1000):
#     a = i //100
#     b = (i-a*100)//10
#     c = (i-a*100-b*10)
#     if pow(a,3)+pow(b,3)+pow(c,3)==i:
#         print('%d为水仙花数！'% i)
# 接收用户输入一个数字，判断直到该数为素数（只能被1和自身整除）时，即停止输入。
# while True:
#     susu=input('请输入一个数字:')
#     if susu.isdigit():
#         susu = int(susu)
#         if susu ==0:
#             print('您输入的数字不能为0，请重新输入！')
#         elif susu > 0:
#             for l in range(2,susu):
#                 if susu % l == 0:
#                     print('%d不为素数！'% susu)
#                     break
#             else:
#                 print('%d是素数!'% susu)
#                 break
#     else:
#         print('您输入的为非数字')

# 列表去重
# set去重
# list1 = [1,6,4,3,7,1,6]
# print(set(list1))
# for 循环去重
# for i in list1:
#     if list1.count(i) > 1:
#         list1.remove(i)
# print(list1)
#
# list2 = []
# for j in list1:
#     if j not in list2:
#         list2.append(j)
# print(list2)
# 字典去重
# list1 = [1,6,4,3,7,1,6]
# dic =  list(dict.fromkeys(list1))
# print(dic)

# 打印空心正方形
# for i in range(5):#for循环控制打印的行数
#     if i==0 or i == 5-1:
#         print('* ' * 5, end='\n')#控制打印的内容
#     else:
#         print('* '+ '  ' * (5-2) + '* ')
#九九乘法表
# for i in range(1,10):#外层循环控制打印几行
#     for j in range(1,i+1):#内层循环控制打印每行的内容
#         print('%d * %d =%2d \t' % (j,i,i*j),end='')
#     print('')

# 冒泡排序
# print('冒泡排序：')
# num = [12,45,24,35,98]
# n =  len(num)
# for i in range(1,n-1):#外层控制比较的轮数
#     for j in range(0,n-i):#内层控制比较的次数
#         if num[j]>num[j+1]:
#             num[j],num[j+1] = num[j+1],num[j]
# print(num)
# a = [1,3,5,8]
# a.append(9)
# print(a)
# a.remove(3)
# print(a)
# a[1:2]=[1,5]
# print(a)
# b =(2,5,6,3,13,3)
# print(b[2])#元祖索引取值
# print(b[-2:])#元祖切片
# print(2 in b)#判断元素是否存在于元祖中
# print(b.count(3))#计数
# 元祖tuple是不可变数据类型，不能单独改变其中某一项的值
# user = (1,'张三',20)
# user[2]=30
# print(user)

# 元祖支持计算
# + 连接:tup3 = tup1 + tup2
# * N 复制并连接：重复N次， tup3 = tup1 * 3
# tup1 = (1,2,3)
# tup2= (4,5,6)
# tup3 = tup1 + tup2
# print(tup3)
# tup4 = tup1 * 5
# print(tup4)
# 内置函数作用于元祖
#     len(tuple):计算元祖元素个数
#     max(tuple)：返回元祖中元素最大值
#     min(tuple):返回元祖中元素最小值
#     sum(tuple):返回元祖中元素的和
# print(len(tup1))
# # print(max(tup1))
# # print(min(tup1))
# # print(sum(tup1))
# for i in tup1:
#     print(i)
# for i in range(len(tup2)):
#     print(tup2[i])
# for i,j in enumerate(tup2):
#     print(i,j)
# extend 扩展 没有返回值
# user = [1,'张三',20,180]
# user1 = [2,'李四',25,170]
# user_info = ['1990-12-01','男']
# user_info1 = ['1995-10-01','女']
# user.extend(user_info)#在原始列表后面追加一个列表，使之合并为一个列表
# print(user)
# user1[2:2] =user_info1#把整个列表插入到一个列表指定位置
# print(user1)
# user1[1:3]=['王五',28]#分片赋值 修改指定范围的值
# print(user1)
# 列表元素删除-pop -索引/remove -元素/del -索引
# 区别：pop有返回值 ；remove 没有返回值  默认返回None。
mm=['1','df','2','gd','df']
# print(mm.pop())
# mm1=mm.pop(1)
# print(mm)
# mm.remove('df')
# print(mm)
# del  要删除的内容，可以用索引，也可以用切片  还可以删除整个list对象（彻底删除）
# del mm[1]
# print(mm)
# del mm[0:2]
# print(mm)
# 清空列表  清空list中的元素
# z=[1,3543,335]
# z.clear()
# print(z)
# 排序   L.sort-原地操作（只修改原始列表顺序），没有返回值，默认返回为None
# numbers =[12,45,36,78,90,49]
# numbers.sort()
# print(numbers)
# reversed()把存放的数据进行翻转
# print(set(numbers))
# numbers.sort(reverse=True)#设置reverse=True后，即实现降序排列
# print(numbers)

# sorted(seq,key,reverse=True),key 需要传入一个函数，这个函数就是你的排序规则 默认不传入后两个参数，按ID正序排列
# sorted函数，有返回值，返回的是排好序的列表，L.sort()不一样，是原地排序
# 对sts按成绩倒序排列
# sts=[(1,'zhangsan',80),(3,'lisi',84),(2,'wangwu',98),(4,'wudi',70)]
# def func(item):
#     return item[-1] #对哪个元素规则进行排序，就须将遍历的该元素return 这里是按成绩排序
# sorted_sts=sorted(sts,key=func,reverse=True)
# print(sorted_sts)
# num_01=[1,4,7]
# num_02=[2,5,8]
# num_01.extend(num_02)
# num = num_01+num_02
# num_01.sort(reverse=True)
# print(num_01)
# 三种方法遍历列表
# for i in numbers:#遍历元素
#     print(i)
# for j in range(len(numbers)):#通过遍历取索引来取元素
#     print(j,numbers[j])
# for i ,j in enumerate(numbers):#通过enumerate函数取索引和元素
# #     print(i,j)

# number = [98,134,24,26,284]
# print(max(number),min(number))
# number.sort(reverse=True)
# print(number)
# print(number[0],number[-1])
# str_1='title=华为春季新品发布会&sign=0&limit=100&status=0&address=国家会议中心&time=2018-03-28'
# print(str_1.split('&'))

#字典是无序数据类型，没有索引，不可以通过索引来取值
# user = {'id':1,'name':'李四','weight':100,'age':35}
# print(user)
# user1 = dict(id=2,name='王五')#字典的定义
# print(user1)
# user2 = {1:['zhangsan',20],2:['lisi',24]}#字典里嵌套列表

# 字典key不能重复,key类型一般是不可变数据类型,int,string
# value没有要求，可以是任意类型，可以重复
# 类似于Json，HashMap
# 可以通过key来获取元素
# print(user['weight'])
# print(user2[1][0])#通过取key值再取索引来获取元素
# fromkeys()快速生成字典 -----*
# a = [1,3,5,6,8,5,1]
#
# b = list(dict.fromkeys(a))
# b=dict.fromkeys(a,1)
# print(dict.fromkeys(a,1))
# 字典是可变数据类型
#dict[key] = value,为字典赋值 在原始字典后追加一个key,value,如果key存在就修改key对应的value，
# 如果key不存在，就在dict中添加key：value键值对
e = ['alphas','spaces','others']
# print(dict.fromkeys(e,0))#快速将多个变量统一生成字典并初始化赋值
# f = dict.fromkeys(e,0)
# f['digts'] = 0 #为字典赋值
# print(f)
# f.setdefault()方法也可以设定默认值  赋值
# urls = {'baidu':'百度','google':'谷歌'}
# urls.setdefault('sogou','搜狗')
# print(urls)
# f.update()方法，如果key已经存在，就更新key对应的value，如果key不存在，就添加key:value
# # 没有返回值，直接拼接在原来的字典中
# urls_new={'JD':'京东','taobao':'淘宝','google':'谷歌中国'}
# # urls.update(urls_new)
# # print(urls)

# dict.get(key,default=None),如果key不存在，返回默认值None/返回指定的default
# print(urls.get('google','该值不存在！'))

# 练习 把字符串'k1:1|k2:2|k3:3'处理成Python字典的形式:{'k3':3,'k2':2,'k1':1}
# str_01='k1:1|k2:2|k3:3'
# str_01_old=str_01.split('|')
# str_01_new={}
# for i in str_01_old:
#     key = i.split(':')[0]
#     value = int(i.split((':'))[-1])
#     str_01_new[key]=value
# print(str_01_new)
# 删除
# 使用key删除字典中的某一个键值对
urls = {'baidu':'百度','google':'谷歌','taobao':'淘宝'}
# del urls['baidu']
# print(urls)
# pop(key) 必须传一个key，返回弹出的key对应的value值
# print(urls.pop('google'))
# popitem(),随机弹出一对键值对，返回元祖（key,value）
# print(urls.popitem())
# 清空字典
# urls.clear()
# print(urls)
# 遍历字典
# for k in urls:
#     print(k,urls[k])
# urls.keys()-->把字典urls中的所有key提取出来，生成一个列表，返回给你
# for i in urls.keys():
#     print(i,urls[i])
# urls.values()-->把字典urls中的所有value提取出来，生成一个列表，返回给你
# for v in urls.values():
#     print(v)
# urls.items()-->[('baidu':'百度'),('google':'谷歌')]

# 从一个字典中获取学霸{'zhangsan':90,'lisi':98,'wangwu':76}
# for k,v in urls.items():
#     print(k,v)
# cj = {'zhangsan':90,'lisi':98,'wangwu':76}
# best = list(cj.keys())[0]
# for k,v in cj.items():
#     if v > cj[best]:
#         best = k
# print(best)

# qc=[1,5,34,5,3,24,1]
# print(set(qc))
# for i in qc:
#     if qc.count(i)>1:
#         qc.remove(i)
# print(qc)
# qc_new=[]
# for i in qc:
#     if i not in qc_new:
#         qc_new.append(i)
# print(qc_new,type(qc_new))
#
# print(list(dict.fromkeys(qc)))
#
# list.remove()#两种方式都可以删除集合中的元素，discard-如果删除的元素不存在，不会报错，remove会报错
# list.discard

# 函数的定义：
# def hello():
#     '''hello function#函数的注释
#     print('hello word')
#     :return:None
#     '''
#     print('hello word')

# 函数必须要调用后才会执行，函数定义必须要在调用之前
# hello()#调用函数
# print(hello.__doc__)通过print函数打印帮助文档
# help(hello)#通过help函数查看函数说明帮助文档
# callable(函数名)函数可以帮助判断 某个函数是否可以被调用，如果可以则返回True
# print(callable(print))
def pow1(x,y):
    return pow(x,y)#返回值 谁调用我 我就把值返回给他 然后存到内存中，以后要用的时候直接调用即可，
    # print 内存中没有变量，下次便不可用了 （后续没处理用print，后续有处理用return）
    #return，返回值可以赋给一个变量，保存在内存中，需要的时候可以再次取出进行计算
print(pow1(4,3))
# 返回值是一个变量，不可能是多个值，只能是以哪种形式去接收，比如列表，元祖等
# 参数（括号中的部分可以是0或者多个值），函数定义时，括号中参数叫形参
# def add(x,y):
#     return x+y
# 调用函数的时候，参数叫实参
# print(add(1,2))
# 可变长度的参数
def print_info(name,age,**tag):#将多传递的参数用*加参数名做区分
    print('姓名：%s,年龄：%d,%s'% (name,age,tag))
    # print('多传递的参数为:',tag)
# print_info('陈翔',20,'四川','本科')#第一种方式调用
# info = ('陈翔',20,'四川','本科')
# print_info(*info)#第二种方式调用 需在此之前定义一个元祖  参数名一个*
# def print_info(name,age,*tag):
# 传入的参数如果是以key=vaule格式，以字典形式传过去的    参数名两个*
# def print_info(name,age,**tag):
print_info(name='陈翔',age=25,address ='四川',xueli='本科')#函数调用

# 经典写法：def print_info(name,age,*args,**tags):这样的话，传入的参数无论是元祖还是字典都可以正常接收，不会报错

# 可选参数/非必填参数
# def 函数名(参数名=默认值) 当参数有多个时，如果调用时只传入一个参数，其他参数不传，当设定默认值后，以默认值计算并返回
# 调用函数时，参数也可以指定

# 参数定义的顺序必须是：必填参数、默认参数、可变参数


# 匿名函数
# lambda 参数：函数返回值
# 2.统计一篇英文文章每个单词的出现频率，并返回出现频率最高的前5个单词及其出现次数(字典形式)
# A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian
dic = 'A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian'
# dic = dic.replace(' ','')
# dic_new={}
# for i in dic:
#     dic_new[i]=dic.count(i)
# dic_new =sorted(dic_new.items(), key=lambda item:item[1],reverse=True)[:5]
# dic_new = dict(dic_new)
# print(dic_new)

# str_list = dic.lower().split()
# counts ={}
# for i in str_list:
#     if i.endswith(',') or i.endswith('.'):
#         i = i[:-1]
#     if i in counts:
#         counts[i]+=1
#     else:
#         counts[i]=1
# top5 = dict(sorted(counts.items(),key=lambda item:item[-1],reverse=True)[:5])
# print(top5)

# 定义一个函数，函数内部调用的是它自己
# 递归函数 -递归调用太深了，栈内存不足，就会报内存溢出错误
# 递归函数，优点-逻辑上容易理解，可读性比较好
# 递归函数包含两个条件：一个叫做结束条件/Base条件，一个叫做递归条件
# def print_n(n):
#     if n==0:
#         return 0
#     print(n)
#     print_n(n-1)
# print_n(10)

# 实现回音效果打印字符串
# 2.编写一个递归函数，达到回声的效果
# 					比如：同志们你们好吗
					# 输出：同志们你们好吗 志们你们好吗 们你们好吗 你们好吗 们好吗 好吗 吗
# def echo(string):
#     if string == '':
#         return 0
#     else:
#         print(string)
#         return echo(string[1:])
#
# echo('我爱北京天安门')

# zip 并行遍历函数
# ids=[1,2,3,4]
# names= ['zhangsan','lisi','wangwu']
# salary=[4000,5000,3000]
# print(list(zip(ids,names,salary)))

# map:将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# map(func,并行遍历的列表),python2.x如果name,salary不传，自动遍历的时候补空,在Python3.x中实现效果和zip函数差不多
# def zuhe(ids,names=None,salary=None):
#     return (ids,names,salary)
# res = map(zuhe,ids,names,salary)
# print(list(res))

# 通过map把这个list所有数字转为字符串
n = [1,2,3,4,5,6,7,8,9]
print(list(map(str,n)))
# reduce(function,遍历的列表) python
# 2.x中存在该函数，在python3.x中如果想使用该函数，需要从functools模块中引用
# 简易的递归函数，归并函数
from functools import reduce
res = reduce(lambda x,y:x+y ,[1,2,3,4,5])
print(res)

# 对象，类的实例化
# 类的对象是模板，对象是类的实例化产物
# 定义一个类
# class 类名(继承的类):
#     类的内容

#     属性  -- 名字，身高，体重
#     成员变量/实例变量，属于每一个实例，实例不同
#     方法  --  考试，吃饭，睡觉

# 基类-object  -- python 中所有对象的父类
class HuiCeStudent(object):
    '''慧测学生类 包含学校姓名 学生信息等'''
    #类变量，默认是所有实例共享的
    school = '慧测'
    # 变量前加双下划线,变量为类的私有变量，别的都不能调用，只能在类里调用
    # 私有变量，在外部，通过类.私有变量 无法访问
    # 在类的内部，是可以正常访问的
    # 添加一个getter函数，来获取私有变量的值
    __xuefei = 8800

    # 初始化方法,构造方法
    # self 指的是实例
    #__init__初始化函数，实例化对象的时候，第一个执行的函数
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_name(self):#成员方法
        print(self.name)
    def print_age(self):
        print(self.age)
    @classmethod   #装饰器
    def print_school(cls):#类方法
        print(cls.school)
        print(cls.__xuefei)
    @classmethod
    def print_xuefei(cls):
        print('学费是%s' % cls.__xuefei)
    @staticmethod   #静态方法
    def add(x,y):
        print(x+y)
    # 类中如果有私有函数，这个私有函数是类独有，只有在类当中可以使用
    def __private(self):
        print(self.name,self.age)
    def __str__(self):
        return '学生姓名：%s，学生年龄：%d' % (self.name,self.age)
    def __len__(self):
        return len(self.name)

# 伪私有
# 类名._类名__私有变量名

# 实例化
stu1 = HuiCeStudent('张三',20)
stu1.print_name()
print(stu1.school)

stu2 = HuiCeStudent('李四',25)
stu2.print_name()
print(stu2.school)

# 类变量，是所有实例共有的，调用时，可以用 类名.类变量 调用
# 也可以通过  实例.类变量 调用

# 成员变量
# 是属于不同的实例，不同实例的成员变量值不同
# 设定成员变量，在__init__(self)中进行设定，self.成员变量
# 在类中进行使用，也需要使用self.成员变量才可以访问

# 方法/函数
# 成员方法，def 函数名(self)
# 类方法，def 函数名(cls)
# 静态方法，def 函数名()
# 调用的是成员方法，使用 实例.成员方法
xiaoming = HuiCeStudent('小明',18)
xiaoming.print_name()
xiaoming.print_age()

# 类方法,  类.类方法，实例.类方法 都可以调用类方法
HuiCeStudent.print_school()
xiaoming.print_school()

# 类.静态方法(),不带self,cls
HuiCeStudent.add(2,3)

# 变量  __特殊变量__
print(HuiCeStudent.__doc__)
print(HuiCeStudent.__bases__)

# HuiCeStudent.print_xuefei()
# HuiCeStudent('张三',20).private()
stu = HuiCeStudent('zhangsan',29)
print(len(stu))
# 特殊方法
# def __方法名__():

# python内置的
# __str__
# toString()

# 2.设计一个汽车类Auto（显示给出一个参数的构造函数--传入品牌名称），
# 有速度属性speed，启动start(显示xx汽车开始运行)、加速speedup(1次速度+10)和停止stop(1次速度-30)方法；

class Auto():
    def __init__(self,logo):
        self.logo = logo
        self.speed = 0
    def start(self):
        print('%s汽车开始运行！'% self.logo)
    def speedup(self):
        self.speed +=10
        return self.speed
    def stop(self):
        if self.speed >=30:
            self.speed -=30
        else:
            self.speed=0
        return self.speed
# tesla = Auto('Tesla')
# print(tesla)
# tesla.start()
# print(tesla.speedup())
# print(tesla.speedup())
# print(tesla.speedup())
# print(tesla.speedup())
# print(tesla.stop())

l = {'bob':90,'wanna':98,'alis':87}
print('bob' in l)
print(l.get('bob'))

