#namedtuple是一个函数，它用来创建一个自定义的tuple对象，
#并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素

#我们用namedtuple可以很方便地定义一种数据类型，
#它具备tuple的不变性，又可以根据属性来引用，使用十分方便


>>> from collections import namedtuple
>>> Point = namedtuple('coordinates',['x','y'])# namedtuple('名称', [属性list])
>>> p=Point(1,2)                     #名称没什么作用，最好跟前面的变量名保持一致
>>> p.x
1
>>> p.y
2
>>> corrdinates.x
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    corrdinates.x
NameError: name 'corrdinates' is not defined

>>> Circle = namedtuple('Circle',['x','y','r'])
#圆心坐标和半径表示一个圆




