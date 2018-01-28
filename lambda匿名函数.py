#原来lambda叫匿名函数，这名字蛮合适


#lambda x(0到随便你几个参数，你高兴就好):y(return的内容)

#因为函数没有名字，不必担心函数名冲突

#也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
q=lambda x : x**3

print(q(5))

#也可把匿名函数作为返回值返回
def build(x,y):
    return lambda:x**2+y**2#返回函数，closure
w=build(3,4)
print(w())


#Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数
