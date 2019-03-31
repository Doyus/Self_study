import threading
import time

# def get_detail_html(url):
#     print("get detail html started")
#     time.sleep(2)
#     print("get detail html end")
#
# def get_detail_url(url):
#     print("get detail url started")
#     time.sleep(2)
#     print("get detail url end")
#
# if __name__ == "__main__":
#     threading1 = threading.Thread(target=get_detail_html, args=("",))
#     threading2 = threading.Thread(target=get_detail_url, args=("",))
#     start_time = time.time()
#     threading1.start()
#     threading2.start()
#     print("last time: {}".format(time.time()-start_time))
    # 时间为0  实际有三个线程  主线程退出子线程并没有退出

"""我们希望主线程退出，子线程也退出"""

# def get_detail_html(url):
#     print("get detail html started")
#     time.sleep(2)
#     print("get detail html end")
#
# def get_detail_url(url):
#     print("get detail url started")
#     time.sleep(4)
#     print("get detail url end")
#
# if __name__ == "__main__":
#     thread1= threading.Thread(target=get_detail_html, args=("",))
#     thread2 = threading.Thread(target=get_detail_url, args=("",))
#     #thread1.setDaemon(True)
#     thread2.setDaemon(True)
#     start_time = time.time()
#     thread1.start()
#     thread2.start()
#     print("last time: {}".format(time.time()-start_time))
#     # 如果只把thead2设为守护进程。那么将不打印替换thread2的结束。但是主线程推出之后
#     # thread1还要等待两秒
#     # 此时将不打印end的内容

"""我们希望主线程等待子线程退出之后自己再退出"""

# def get_detail_html(url):
#     print("get detail html started")
#     time.sleep(2)
#     print("get detail html end")
#
# def get_detail_url(url):
#     print("get detail url started")
#     time.sleep(4)
#     print("get detail url end")
#
# if __name__ == "__main__":
#     thread1= threading.Thread(target=get_detail_html, args=("",))
#     thread2 = threading.Thread(target=get_detail_url, args=("",))
#     #thread1.setDaemon(True)
#     #thread2.setDaemon(True)
#     #start_time = time.time()
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()
#
#     print("last time: {}".format(time.time()-start_time))
#     # 如果只把thead2设为守护进程。那么将不打印替换thread2的结束。但是主线程推出之后
#     # thread1还要等待两秒
#     # 此时将不打印end的内容


"""通过继承thread来实现多线程"""

class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_html")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    