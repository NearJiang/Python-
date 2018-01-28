#要1到10的list很简单
print(list(range(1,11)))

#想要1到10每个数的平方呢
L=[]
for i in range(1,11):
	L.append(i**2)
print(L)

#我们python推崇的是什么！！！ 大简至上！
print([i**3 for i in range(1,11)])#这边的[]是把结果给【】起来，列表生成式嘛，得由列表嘛
#把要生成的元素放到前面，后面跟for循环，就可以把list创建出来

print([i**3 for i in range(1,11) if i % 2 ==0])#再加上if判断

print([x+y for x in 'ABC' for y in 'abc'])#这里的加是让被加的元素合起来，变成一个字符串

print([x*y for x in (1,2,3) for y in (4,5,6)])#两层循环

#上面iteration迭代里用
d={'a':1 ,'b':2 ,'c':3}
for k,v in d.items():
	print(k,'=',v)#参数和字符串间一定要用逗号，隔开！！切记！！
#我们用列表生成式试试
print([k+"="+v for k,v in d.items()])#这边的+表示让k，+，v这三个合成：k=v
