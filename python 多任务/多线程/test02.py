# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-09-30 11:25:06
# @Last Modified by:   Marte
# @Last Modified time: 2018-09-30 11:38:44
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

    time.sleep(1)


    t2.start()

    time.sleep(1)
    print(threading.enumerate())

if __name__ == '__main__':
    main()

#线程的运行是没有先后顺序的