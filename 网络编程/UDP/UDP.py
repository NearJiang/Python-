import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
#创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP
#绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
#recvfrom()方法返回数据和客户端的地址与端口，
#这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端

#客户端使用UDP时，首先仍然创建基于UDP的Socket，
    #然后，不需要调用connect()，直接通过sendto()给服务器发数据

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
#从服务器接收数据仍然调用recv()方法

#UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，
#也就是说，UDP的9999端口与TCP的9999端口可以各自绑定
