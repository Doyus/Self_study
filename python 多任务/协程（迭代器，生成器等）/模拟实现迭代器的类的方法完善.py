# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-09-30 21:28:05
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-01 09:46:31
from collections import Iterable
from collections import Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        # 如果想要一个对象称为一个可以迭代的对象，即可以使用for,那么必须实习__iter__方法
        return self

    def __next__(self):
        if self.current_num < len(self.names):

            ret = self.names[self.current_num]
            self.current_num += 1
            return ret

        else:
            raise StopIteration(" error")


classmate = Classmate()

classmate.add("老三")
classmate.add("王三")
classmate.add("张三")

# print("判断classmate是否是可以迭代的对象：",isinstance(classmate,Iterable))

# classmate_iterator = iter(classmate)

# print("判断classmate是否是可以迭代的对象："，isinstance(classmate_iterator,Iterator))

# iter(classmate)


for name in classmate:
    print(name)
    time.sleep(1)

















# for temp in xxx_obj:
#     pass

# 1. 判断xxx_obj是否可以迭代：只要创建它的类里边有__iter__这个方法，那么它就可以迭代
# 2. 在第一步成立的前提下，调用iter函数，得到xxx_obj对象的__iter__方法得到的返回值(引用)：
# 如果__iter__返回的那个引用(对象)里边实现了__iter__和__next__方法，那么这个就是j迭代器（ClassIterator） 每一次for循环，就是调用__next__方法
#
# 3. __iter__ 方法的返回值就是一个迭代器