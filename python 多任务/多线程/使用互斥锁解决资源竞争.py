# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-09-30 12:09:05
# @Last Modified by:   Marte
# @Last Modified time: 2018-09-30 15:05:52
#
# 是否需要global进行声明，要看是否对全局变量的指向进行了修改，如果需要让全局变量指向新的变量，则需要global，如果只是对原来指向的东西里边的数据进行增减，则不需要global
#

g_num = 0
#
import threading
import time



def test1(num):
    global g_num
    #上锁，如果之前没有被上锁，那么此时，上锁成功
    #如果上锁之前，已经被上锁了，那么此时会堵塞在这里，直到这个锁被解开
    # mutex.acquire()
    for i in range(num):
        g_num += 1

    #解锁
    # mutex.release()
    print("-------in test1 g_num%d----"%g_num)

def test2(num):
    global g_num
    # mutex.acquire()
    for i in range(num):
        g_num += 1

    # mutex.release()
    print("-------in test2 g_num%d----"%g_num)



#创建一个互斥锁，默认没有上锁
mutex = threading.Lock()

def main():

    t1 = threading.Thread(target=test1,args=(100000,))
    t2 = threading.Thread(target=test2,args=(100000,))

    t1.start()
    t2.start()
    time.sleep(5)
    print('----in main Thread g_num = %d--'%g_num)

if __name__ == '__main__':
    main()