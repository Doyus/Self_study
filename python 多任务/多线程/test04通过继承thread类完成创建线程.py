# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-09-30 11:55:39
# @Last Modified by:   Marte
# @Last Modified time: 2018-09-30 12:08:40
import threading
import time
#与 thread(target=函数)的创建方式区别开
#run方法会自动调用
class MyThread(threading.Thread):
    def run(self):#run这个名字是固定的

        for i in range(3):

            time.sleep(1)
            msg = "I'm" + self.name + '@' + str(i)
            print(msg)

    def login(self):
        pass

    def register(self):
        pass

    # 这里注意：后边的login和register是无法调用的，因为一个线程只能执行一个方法，这种方式会隐式调用里边的run方法，而且必须名是run,如果真想调用，可以在run里边调用login和register方法达到那个效果


if __name__ == '__main__':
    t = MyThread()
    t.start()

