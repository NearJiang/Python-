from io import StringIO
#写
f=StringIO()

f.write('jiang')
f.write(' ')#空格
f.write('baba')


print(f.getvalue())

#读
f=StringIO('jiangbaba\nlove\nqibaobao')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
