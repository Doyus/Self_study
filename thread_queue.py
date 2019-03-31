# 线程间通信
import threading
import time

detail_url_list = []

def get_detail_html(detail_url_list):
    # 爬取文章详情页
    # 这种方式没有达到并发的要求
    # for url in detail_url_list:
    #     print("get detail html started")
    #     time.sleep(2)
    #     print("get detail html end")
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print("get detail html started")
            time.time(2)
            print("get detail html end")

def get_detail_url(detail_url_list):
    # 爬取文章列表页
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            detail_url_list.append("http://projectsedu.com{id}".format(id=i))
        print("get detail url end")

if __name__ == "__main__":
    thread_detail_url = threading.Thread(target=get_detail_url,args=(detail_url_list,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html,args=(detail_url_list,))
        html_thread.start()

