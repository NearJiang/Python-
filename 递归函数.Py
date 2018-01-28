#如果一个函数在内部调用自己本身，这个函数就是递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)  #这个函数定义的是n*（n-1）*到1
print(fact(5))
#fact(5)
#5 * fact(4)
#5 * (4 * fact(3))
#5 * (4 * (3 * fact(2)))
#5 * (4 * (3 * (2 * fact(1))))
#5 * (4 * (3 * (2 * 1)))
#5 * (4 * (3 * 2))
#5 * (4 * 6)
#5 * 24
#120


def months(n):
	while n<1:
		print('输入有误')
		return -1
	if n==1 or n==2:
		return 1
	else:
		return (months(n-1)+months(n-2))
question=int(input('你想知道第几个月的小兔子诞生量？：'))
print('%d月的小兔子诞生量为%d'%(question,months(question)))
input('press[enter]')


#m(5)
#m(5-1=4)+m(5-2=3)
#m(4-1=3)+m(4-2=2) + m(3-1=2)+m(3-2=1)#m(1和2=1)
#m(3-1=2)+m(3-2=1)+1+1+1
#1+1+1+1+1
# return 5

#汉诺塔
def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从 x 移动到 y 上
        print(x,'-->',z)#将最低下的最后一个盘子从 x 移动到 z 上
        hanoi(n-1,y,x,z)#将 y 上的n-1个盘子移动到 z 上
n = int(input('输入汉诺塔的大金片数：'))
hanoi(n,'1','2','3')#直接调用函数，不需要print
input('press[enter]')
