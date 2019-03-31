# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-05 20:55:10
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-05 21:11:17
import threading
import random
import time

qMoney = 1000
qLock = threading.Lock()

class Producer(threading.Thread):
    def run(self):
        global qMoney
        while True:
            money = random.randint(100,1000)
            qLock.acquire()
            qMoney += money
            print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(),money,qMoney))
            qLock.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        while True:
            global qMoney
            money = random.randint(100,1000)
            qLock.acquire()
            if qMoney >= money:
                qMoney -= money
                print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(),money,qMoney))
            qLock.release()
            time.sleep(0.5)
def main():
    for x in range(3):
        t = Consumer(name="消费者线程%d"%x)
        t.start()

    for x in range(5):
        t = Producer(name="生产者线程%d"%x)
        t.start()



if __name__ == '__main__':
    main()