import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0",8000)) # 传一个元组
server.listen()

def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        re_data = input("服务器输入>>>")
        sock.send(re_data.encode("utf8"))
  # 准备接受数据
while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock,args=(sock,addr))
    client_thread.start()
    # data = sock.recv(1024)
    # print(data.decode("utf8"))
    # sock.send("hello{}".format(data).encode("utf8"))

# 获取重客户端发来的数据，一次获取一kb的数据

#print(data.decode("utf8"))
# server.close()
# sock.close()

