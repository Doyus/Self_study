# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-09-30 12:09:05
# @Last Modified by:   Marte
# @Last Modified time: 2018-09-30 13:16:25
#
# 是否需要global进行声明，要看是否对全局变量的指向进行了修改，如果需要让全局变量指向新的变量，则需要global，如果只是对原来指向的东西里边的数据进行增减，则不需要global
#
#
#
#
import threading
import time

g_num = 100

def test1():
    global g_num
    g_num += 1
    print("--------------in test1 g_num=%d=-----"%g_num)

def test2():
    print("--------------in test2 g_num=%d=-----"%g_num)

def main():

    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("-----in main thread g_num = %d ---0"%g_num)

if __name__ == '__main__':
    main()