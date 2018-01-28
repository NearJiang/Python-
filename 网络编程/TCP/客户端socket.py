import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))#注意参数是一个tuple，包含地址和端口号
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()

#创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6

#SOCK_STREAM指定使用面向流的TCP协议，
#这样，一个Socket对象就创建成功，但是还没有建立连接

#客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。
#新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址，
#但是怎么知道新浪服务器的端口号呢

#答案是作为服务器，提供什么样的服务，端口号就必须固定下来

#80端口是Web服务的标准端口

#接收数据时，调用recv(max)方法，一次最多接收指定的字节数，
#因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。

#当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了

#接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，
#把HTTP头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
