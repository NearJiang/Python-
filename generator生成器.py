#要创建一个generator，有很多种方法。
#生成器表达式：很简单，只要把一个列表生成式的[]改成()

w=(x**2 for x in range(10))
#通过next()函数获得generator的下一个返回值
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
#直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误

#上面这种不断调用next()实在是太变态了，
#正确的方法是使用for循环，因为generator也是可迭代对象
w=(x**2 for x in range(10))
for i in w:
	print(i)

#生成器函数：在函数中出现了yield关键字，那么该函数就不再是普通函数了
#而是生成器函数
def fibonacci():
	a=b=1
	yield a
	yield b
	while True:
		a,b=b,a+b
		yield b

for num in fibonacci():
	if num >100:
		break
	print(num)