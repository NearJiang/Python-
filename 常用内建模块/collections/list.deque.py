#一句话，deque就是快速插入或删除一个list的头部或尾部的

#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了
#因为list是线性存储，数据量大的时候，插入和删除效率很低


#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈

>>> from collections import deque
>>> q = deque(['a','b','c'])
>>> q.append('x')#默认插在尾部
>>> q
deque(['a', 'b', 'c', 'x'])
>>> q.appendleft('y')#插在头部
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
>>> q.appendcenter(5)#不能向中间插入
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    q.appendcenter(5)
AttributeError: 'collections.deque' object has no attribute 'appendcenter'

>>> q.pop()#删尾部
'x'
>>> q
deque(['y', 'a', 'b', 'c'])
>>> q.popleft()#删头部
'y'
>>> q
deque(['a', 'b', 'c'])
>>> q.pop(1)#不能向list那样  想删哪一个就删哪一个
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    q.pop(1)
TypeError: pop() takes no arguments (1 given)
