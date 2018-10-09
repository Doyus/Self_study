# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-09-30 11:25:06
# @Last Modified by:   Marte
# @Last Modified time: 2018-09-30 11:52:48
import threading
import time
def test1():
    for i in range(5):
        print('***********test1********%d****'% i)

def test2():
    for i in range(5):
        print('***********test2********%d*****'% i)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        if(len(threading.enumerate())):
            break

        time.sleep(1)

if __name__ == '__main__':
    main()

#如果创建thread时执行的函数，运行时结束那么意味着子线程结束
#
#当调用thread的时候，不会创建线程，start时候才开始