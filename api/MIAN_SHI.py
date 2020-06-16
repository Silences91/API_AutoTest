# -*- coding: utf-8 -*-
# @Author : DONGYAC
# @Time : 2020-05-27 下午 19:59
# @File : MIAN_SHITI.py
# pypython合并两个列表 有两种方式：
# 1、使用extend   extend是在原列表 原地操作 a.extend(b)
# 2、使用+   + 是生成新的列表
fm_100 =[100]
fm_50 = [50]
FM_100 = fm_100 * 99
FM = FM_100 + fm_50 #使用+
# FM_100.extend(fm_50)#使用extend
for f in FM:
    if f == 50:
        print(FM.index(f))
z = [33,44,66,88,77,11,55,22]
print(z.index(55))