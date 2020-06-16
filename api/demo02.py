# -*- coding:utf8 -*-
# 四种去重:
# jc = [1,34,24,2,1,34,26]
# for i in jc:
#      if jc.count(i)>1:
#          jc.remove(i)
# print('第一种:',jc)
#
# jc_new = []
# for i in jc:
#     if i not in jc_new:
#         jc_new.append(i)
# print('第二种:',jc_new)
#
# print('第三种:',set(jc))
#
# print('第四种:',list(dict.fromkeys(jc)))

# 冒泡排序
# r = [1,87,24,34,14,46,35]
# for i in range(1,len(r)):
#     for j in range(0,len(r)-i):
#         if r[j] > r[j+1]:
#             r[j],r[j+1] = r[j+1],r[j]
# print(r)

# 输入数字，计算1到n的阶乘
# 第一种:for 循环
# num = input('请输入一个数字：')
# if num.isdigit():
#     num = int(num)
#     total = 1
#     if num > 1:
#         for i in range(1,num):
#             i+=1
#             total *=i
#         print(total)
#     if num <=1:
#         print('请输入大于1的整数。')
# else:
#     print('您输入的不是数字，请重新输入！')
# 第二种：while循环
# while True:
#     num = input('请输入一个数字:')
#     if num.isdigit():
#         num=int(num)
#         total  = 1
#         for i in range(1,num):
#             i +=1
#             total *=i
#         print(total)
#         break
# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%2d'% (j,i,i*j),end=' ')
#     print('')

# number = [1,2,3,4]
# age = [24,25,30,14]
# score = [90,93,98,67]
# p = (zip(number,age,score))
# print(list(p))

# 两行代码实现输出1-100之间的奇数
# for i in range(1,100,2):
#     print(i)
# 输出1-100之间的偶数，以列表形式正序输出
# x=[]
# for j in range(100,0,-2):
#     x.append(j)
#     x.sort()
# print(x)
# 函数定义和调用
def my_abs(x):
    '''求绝对值方法'''
    if not isinstance(x, (int, float)):#我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# print(my_abs(-2))
print(pow(3,3))
# 自定义函数 默认参数
def student(name,age,gender='F',city='beijing'):
    print('name:',name)
    print('age:',age)
    print('gender:',gender)
    print('city:',city)
student('陈东阳',28)

# 函数-可变参数
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1,2,3]
print(calc(*nums))#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去；*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
# 关键字参数
# 关键字参数可以扩展函数的功能
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Adam',45,gender='M',job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}#另一种简化的写法
person('jack',30,**extra)#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# # 调用方式如下：
person('Jack', 24, city ='Beijing', job ='Engineer')
def person(name, age, *args,city,job):
    print(name, age, args, city, job)
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer')
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

# 练习题：以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x,*args):
    i = 1
    for  n in args:
        i = n * i
    return x * i
print(product(3,4,5))
# 递归函数 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def print_n(n):
    if n==0:
        return 0
    print(n)
    print_n(n-1)
# print_n(10)
# 递归函数 计算阶乘
def fact(n):
    if n==1:
        return 1
    print(n)
    return n * fact(n - 1)
# fact(5)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:3])

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    max=L[0]
    min=L[0]
    for i in L:
        if i >max:
            max = i
        elif i< min:
            min = i

    return (max, min)
L=[1,46,343,4,24,23]
# print(findMinAndMax(L))

# [1,3,4,5,2,3,12,3,21,34,23]查找列表中元素重复的个数
J= [1,3,4,5,2,3,12,3,21,34,23,3]
# 第一种：通过遍历列表和count方法 统计重复个数
# for i in J:
#     if J.count(i) > 1:
#         nums = J.count(i)
# print('重复元素的个数为%d' % nums)
# 第二种：通过Counter方法遍历列表，并将每个元素的个数以字典方式展示
# from collections import Counter
# li = [1, 3, 4, 5, 2, 3]
# a = Counter(li)
# print(a)
# 第三种：定义个空字典，将遍历得到的重复的元素写入字典
# zk = {}
# for i in J:
#     if J.count(i) > 1:
#         value =  J.count(i)
#         key = i
#         zk[key] = value
# for k,v in zk.items():
#     print('333重复元素%d 的个数为%d' % (k,v))

# 列表生成式
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print(list(range(1, 11)))
# 要生成[1x1, 2x2, 3x3, ..., 10x10],列表生成式则可以用一行语句代替循环生成上面的list
print([x * x for x in range(1, 11)]) #写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print([x * x for x in range(1, 11) if x % 2 == 0]) #for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower()for x in L1 if isinstance(x,str)]#使用内建的isinstance函数可以判断一个变量是不是字符串,通过添加if语句保证列表生成式能正确地执行
print(L2)

# 去除字典中value重复的项	{'zhangsan':100, 'lisi':65, 'tianlaoshi':65, 'liulaoshi':99}

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
#     name1 = name[0].upper()
#     name2 = name[1:].lower()
#     name =  name1+name2
#     return name
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize,L1))
# print(L2)

# filter Python内建的filter()函数用于过滤序列。
# 在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 请用sorted()对以下列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)

# 请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1
# L = list(filter(is_odd, range(1, 20)))

print(list(filter(lambda x:x % 2 ==1, range(1,20))))

