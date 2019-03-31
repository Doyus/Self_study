# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-09-30 16:34:35
# @Last Modified by:   Marte
# @Last Modified time: 2018-09-30 16:45:39
import multiprocessing

def download_from_web(q):
    '''下载数据'''
    data = [11,22,33,44]
    #向队列中写入数据
    for temp in data:
        q.put(temp)
    print("---下载器已经下载完了数据并且存入---")
def analysis_data(q):
    """数据处理"""
    #从队列中获取数据
    waitting_analysis_data = list()
    while True:
        data = q.get()
        waitting_analysis_data.append(data)

        if q.empty():
            break
    print(waitting_analysis_data)

    #模拟数据处理

def main():
    #1.创建一个队列
    q = multiprocessing.Queue()
    #2.创建多个进程，将队列的引用当作实参传递到里面
    p1 = multiprocessing.Process(target=download_from_web,args=(q,))
    p2 = multiprocessing.Process(target=analysis_data,args=(q,))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()
    q = multiprocessing.Queue()