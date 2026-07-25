import socket
import random
host = socket.gethostname()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = '127.0.0.1'
#s = socket.socket()
port = 12345
list = ["你好啊人","我饿了饭饭","我饱了😄","我困了，要😴了","不要和我👋🏻会🐭的"，"好的好的，在的在的"]


s.bind((host,port))
s.listen(5)
sock,addr = s.accept()
print('连接已经建立')
info = sock.recv(1024).decode()
while info != 'byebye':
    if info:
        print('接收到的内容：'+info)
    #send_data = input('输入发送的内容：')
    send_data = list[random.randint(0,5)]
    sock.send(send_data.encode())
    if send_data == 'byebye':
        break
    info = sock.recv(1024).decode()
sock.close()
s.close()
