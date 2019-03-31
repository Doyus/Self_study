# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-01 10:30:40
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-01 10:41:51
class Fibonacci(object):
    def __init__(self,all_num):
        self.all_num = all_num
        self.count_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count_num < self.all_num:
            ret = self.a
            self.a, self.b = self.b,self.a + self.b
            self.count_num += 1

            return ret
        else:
            raise StopIteration

finonacci = Fibonacci(10)

for i in finonacci:
    print(i)