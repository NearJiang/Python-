#既然变量可以指向函数(如：f=abs())，函数的参数能接收变量(如：f(-5)=5)
#那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x, y, f):
    return f(x) + f(y)

print(add(-5,6,abs))
#把函数作为参数传入，这样的函数称为高阶函数，
#函数式编程就是指这种高度抽象的编程范式
