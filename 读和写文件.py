f = open('/Users/michael/test.txt', 'r')
f.read()
f.close()


with open('/path/to/file', 'r') as f:
    print(f.read())

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，
#反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便

f = open('/Users/michael/test.jpg', 'rb')#图片/视频
f.read()

f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')#非UTF-8
f.read()





>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')

    #以'w'模式写入文件时，如果文件已存在，会直接覆盖
    #如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
    with open('/Users/michael/test.txt', 'a') as f:
