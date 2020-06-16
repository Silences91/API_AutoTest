# -*- coding: utf-8 -*-
# @Author : DONGYAC
# @Time : 2020-06-07 下午 23:05
# @File : CheckPoint.py
#自定义 检查点函数 --原生断言 封装和改造

import unittest

class CheckPoint(unittest.TestCase):
    def __init__(self):
        self.flag = 0
        self._type_equality_funcs = {}
    def equal(self, f, s):
        try:
            self.assertEqual(f, s)
            print(f'检查点运行成功，实际结果为：[{f}],预期结果为[{s}]')
        except:
            print(f'检查点运行失败，实际结果为：[{f}],预期结果为[{s}]')
            self.flag +=1

    def less_then(self, f,s):
        try:
            self.assertLess(f, s)
            print(f'检查点运行成功，实际结果为：[{f}],预期结果为[{s}]')
        except:
            print(f'检查点运行失败，实际结果为：[{f}],预期结果为[{s}]')
            self.flag +=1

    def result(self):
        if self.flag>0:
            self.assertTrue(False)
            # raise Exception ('断言出现错误！') 手动抛异常