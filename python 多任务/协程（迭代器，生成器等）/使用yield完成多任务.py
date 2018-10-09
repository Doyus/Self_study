# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-01 13:39:01
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-01 14:00:32
import time

def tast_1():
    while True:
        print('------1-----')
        time.sleep(0.1)
        yield

def task_2():
    while True:
        print('----2-----')

        time.sleep(0.1)
        yield

def main():
    t1 = task_1()
    t2 = task_2()
    while True:
        next(t1)
        next(t1)

if __name__ == "__main__":
    main()

# 协程的最大特点,调用一个任务就像调用一个函数一样,它切换的资源最少,而进程相当多,线程次之