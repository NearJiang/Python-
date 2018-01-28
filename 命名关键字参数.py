#如果要限制关键字参数的名字，就可以用命名关键字参数#

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
# *后面的参数被视为命名关键字参数

def person(name, age, *, city, job):#只接收city和job作为关键字参数
    print(name, age, city, job)

def person(name, age, *args, city, job):#如果函数定义中已经有了一个可变参数*args，
    print(name, age, args, city, job)#后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
#命名关键字参数必须传入参数名
>>> person('Jack', 24, city='Beijing', job='Engineer')

#命名关键字参数配合默认参数可以有缺省值，从而简化调用

def person(name, age, *, city='Beijing', job):
>>> person('Jack', 24, job='Engineer')

>>> Jack 24 Beijing Engineer

