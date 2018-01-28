#可变参数允许你传入0个或任意个参数，
#这些可变参数在函数调用时自动组装为一个tuple（）

#关键字参数允许你传入0个或任意个含参数名的参数，
#这些关键字参数在函数内部自动组装为一个dict{ }

def person(name,age,**kw):#关键字参数kw
    print('name:',name,'age:',age,'other:',kw)#字符串与参数间必须得用逗号隔开

print(person('Michael', 30))#在调用该函数时，可以只传入必选参数,
#  name: Michael age: 30 other: {}   关键字参数用个{}表示

#也可以传入任意个数的关键字参数
print(person('Bob', 35, city='Beijing'))#插入形式为xxx='yyy'！！！！！！！！！！
#name: Bob age: 35 other: {'city': 'Beijing'}

print(person('Adam', 45, gender='M', job='Engineer'))
#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}


#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去

extra = {'city':'suzhou','job':'student'}#{}里只能冒号，没有等号=
print(person('Near',22,city=extra['city'],job=extra['job']))
#city=extra['city']：插入city参数，value=extra里的city的值，表现形式为'city': 'suzhou'
#name: Near age: 22 other: {'city': 'suzhou', 'job': 'student'}

#上面先复杂，ok：
print(person('Near', 22, **extra))
#**extra表示把extra这个dict的所有key-value
#用关键字参数传入到函数的**kw参数，kw将获得一个dic
