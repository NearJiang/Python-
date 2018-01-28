#map()函数接收两个参数，一个是函数(下面的q)，一个是Iterable可迭代对象(下面的list)
def q(x):
    return x**2

j=map(q,[1, 2, 3, 4, 5, 6, 7, 8, 9])#把list中的元素以q的方法再以map形式赋值给j

print(list(j))
#map()传入的第一个参数是q，即函数对象本身。


print(list(map(str,[1, 2, 3, 4, 5, 6, 7, 8, 9])))
#吧list中的元素以str的方法再以mao的形式表现出来

