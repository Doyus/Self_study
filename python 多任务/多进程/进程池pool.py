# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-09-30 17:15:19
# @Last Modified by:   Marte
# @Last Modified time: 2018-09-30 17:49:17
#
# 当需要创建子进程数量不多时，可以直接利用multiprocessing 中的multiprocessing模块动态生成多个进程，但如果是上百甚至上千个目标，手动创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的pool方法。
#
from multiprocessing import Pool
import os, time, random

def worker(msg):
    t_start = time.time()
    print("%s 开始执行，进程号为%d"%(msg,os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(1)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))

po = Pool(3) #定义一个进程池，最大进程数3

for i in range(0,5):
    # Pool().apply_async(要调用的目标，（传递给目标的参数数组，))
    po.apply_async(worker,(i,))

print("-----start------")
po.close()#关闭进程池，关闭后po不再接受新的请求
po.join()#等待po中断所有子进程执行完成，必须放在close语句之后
print("---end---")