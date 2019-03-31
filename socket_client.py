import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",8000)) # 传一个元组
while True:
    datas = input("客户端输入>>>>")
    client.send(datas.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))

#client.close()
