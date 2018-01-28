#reduce接受2个函数，跟map一样，前面为函数，后面为iterable
from functools import reduce
def add (x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))
#reduce把结果继续和序列的下一个元素做累积计算
#就是先1,3得到4再4,5这么下去
#当然求和直接sum(iterable,start)#start不写默认为0
print(sum([1,5,9,10],5))


#把序列[1, 3, 5, 7, 9]变换成整数13579
def trans(x,y):
    return x*10+y
print(reduce(trans,[1,3,5,7,9]))
#1 3 --10 3 --13
#13 5 -- 130 5 --135
#135 7 --1350 7 --1357
#1357 9 --13570 9 --13579
