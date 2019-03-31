import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
'''
1. epoll 并不代表一定比select好， 在高并发的情况下，连接活跃度不是很高， epoll比select好
2. 并发性不高，同时连接很活跃， select比epoll

通过非阻塞式io实现http请求
'''
# 使用select完成http请求

selector = DefaultSelector()
stop = False
urls = []
class Fetcher:
    def __init__(self):
        pass

    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path,self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            print("请求头>>>","*"*50)
            print(data.split("\r\n\r\n")[0])
            print("请求体>>>", "*" * 50)
            print(data.split("\r\n\r\n")[1])
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        #url - urlparse(url)
        # 通过socket请求html
        self.url = urlparse(url)
        self.host = self.url.netloc
        self.path = self.url.path
        self.data = b""
        if self.path == "":
            self.path = "/"
        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host,80))
        except BlockingIOError as e:
            pass

        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

def loop():
    #1. select本身是不支持register模式
    #2. socket 状态变化以后的回调是由程序员完成的
    #3. 事件循环，不停的请求socket的状态并调用对应的回调函数
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            callback = key.data
            callback(key)

'''回调+事件循环+select(poll\epoll)'''

if __name__ == "__main__":

    import time
    start_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print(time.time()-start_time)