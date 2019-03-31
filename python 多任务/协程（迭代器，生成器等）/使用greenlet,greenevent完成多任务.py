# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-01 14:01:48
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-01 14:34:26
""" 明白核心原理是用yield实现的,为了更好的使用协程来完成多任务,python中greenlet模块对其封装,从而使得切换任务变得更加简单
pip install greenlet 进行安装
"""

from greenlet import greenlet
import time

def test1():
    while True:
        print('-----A-----')
        gr2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print('-----B------')
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()


"""gevent 是使用greenlet进行的封装，greenlet是使用yield进行封装"""

import gevent

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)

def f2(n):
for i in range(n):
    print(gevent.getcurrent(), i)
    gevent.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)

print("----1-----")
g1 = gevent.spawn(f1, 5)
print("----2-----")
g1 = gevent.spawn(f2, 5)
print("----3-----")
g1 = gevent.spawn(f3, 5)
print("----4-----")
g1.join()
g2.join()
g3.join()

"""gevent的好处就是如果遇到延时，会自动切换任务，延时不可以用time.sleep,而应该用gevent.sleep()方法

协程依赖于线程，线程依赖于进程"""


'''补丁版'''
from gevent import monkey
import random
import time
import gevent

#有耗时操作时需要

monkey.patch_all() #将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

# 这时候就能用time.sleep()了，其他耗时操作的接口也不用专门都改成gevent的


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)

def f2(n):
for i in range(n):
    print(gevent.getcurrent(), i)
    gevent.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)

print("----1-----")
g1 = gevent.spawn(f1, 5)
print("----2-----")
g1 = gevent.spawn(f2, 5)
print("----3-----")
g1 = gevent.spawn(f3, 5)
print("----4-----")
g1.join()
g2.join()
g3.join()
