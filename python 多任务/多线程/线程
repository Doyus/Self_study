# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-09-30 10:53:17
# @Last Modified by:   Marte
# @Last Modified time: 2018-09-30 11:02:19
import time
import threading
def sing():

    for i in range(5):

        print('正在唱：安河桥北')
        time.sleep(1)

def dance():

    for i in range(5):

        print('正在跳舞：芭蕾')
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()



if __name__ == "__main__":
    main()
