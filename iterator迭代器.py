#凡是可作用于for循环的对象都是iterable可迭代对象类型
#凡是可作用于next（）函数的对象都是iterator迭代器类型

i=[1,2,3,4]
for x in i:
    pass
#等价于：
w=iter(i) #list、dict、str等是可迭代对象，可以套在iter()里，变成iterator
while True:
    try:
        x=next(w)
    except StopIteration:
        break 

#3句箴言：
#iterable是可迭代的
#iterator是迭代器
#可迭代的对象可以通过iter()函数转化为迭代器