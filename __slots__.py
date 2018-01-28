#允许对Student实例添加name和age属性
class Student(object):
    __slots__ = ('name', 'age')

>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'

#slots狭缝，缝外的一律对calss 类不管用！！！
