def int1(x):#base默认为10
    return int(x)
print(int1('46'))

def int2(x,base=2):#x的输入形式为2进制的
    return int(x,base)#base默认为10，x输出形式为10进制的
print(int2('1000000'))

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()

import functools
int2 = functools.partial(int,base=2)#①
print(int2('1010101'))
print(int2('1010101',base=10))#在函数调用时传入其他值
#function.partial的作用就是，设置默认值。
>>> kw={'base':2}
>>> int('1010101',**kw)
85
#上面设置base=2为默认值
#int2('1010101')=kw={'base':2}再int('1010101',**kw)

>>> import functools
>>> max2 = functools.partial(max, 10)#②
>>> max2(2,5,9)
10
#这里面就设立了10为默认值，无论你max2（）里有哪些数，10会作为*args的一部分
#加到左边，max2（2，5，9）=args=（10，2，5，9）再max（*args）


#①：定义int2，partial（你要定义的函数，你要设置的默认值）
#定义为int，默认base=2，以后用int2，就默认你括号里是2进制的数了
#②：定义max2，先定义个我想要的函数max，再在里面设置个默认值10，以后用max2就自动
#有10这个数了
