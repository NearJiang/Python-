#迭代是通过for ... in来完成的
#Python的for循环不仅可以用在list或tuple上
#dict
d={'a':1 ,'b':2 ,'c':3}
for key in d:
	print(key)
#dictdict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
for value in d.values():
	print(value)
for k,v in d.items():
	print(k,v)

#符串也是可迭代对象
for i in 'absdsa':
	print(i)

#enumerate列举 把一个list变成索引-元素对（0 a）
for i , value in enumerate(['a','b','c']):
	print(i, value)

for x, y in [(1,2),(3,4).(5,6)]:
	print(x, y)

