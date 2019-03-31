import time
import threading
from queue import Queue

# 线程间通信

def get_detail_html(detail_url_list):
    # 爬取文章详情页
    # 这种方式没有达到并发的要求
    # for url in detail_url_list:
    #     print("get detail html started")
    #     time.sleep(2)
    #     print("get detail html end")
    while detail_url_queue.empty():
        url = detail_url_queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")
        detail_url_queue.task_done()




def get_detail_url(detail_url_queue):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_queue.put("http://projectsedu.com{id}".format(id=i))
        print("get detail url end")

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url,args=(detail_url_queue,))
    thread_detail_url.start()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html,args=(detail_url_queue,))
        html_thread.start()

    start_time = time.time()

    detail_url_queue.join()

    print("结束")

