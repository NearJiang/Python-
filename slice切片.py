L = ['Near', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前三个我们可以：
print(L[0],L[1],L[2])
#还可以循环：
Q=[]
n=3
for i in range(n):
	Q.append(L[i])#list一定得是[] 不是括号（）！！！！！！！！！！
print(Q)
#都太麻烦！！！！祭出SLICE大法
print(L[0:3])
print(L[:3])#从0开始就可以不写了
print(L[1:3])
print(L[1:])
#既然list能[-1]表示最后一个，理所当然！
print(L[-2:])
print(L[:-3])#记得冒号后面的数要-1，这边也就是-4倒数第四个
#x：y 从x开始，到y-1  x不写默认为0，y不写默认到最后
w=list(range(10))
print(w[:9:2])#从0开始到8，没跳2个显示一下
print(w[::3])#中间不写就默认所有数，然后后面那个随你跳咯

#tuple也可以用切片操作，只是操作的结果仍是tuple
a=(0, 1, 2, 3, 4, 5)
print(a[:3])
#字符串也可以用切片操作，只是操作结果仍是字符串
print('abcdefg'[:1])

#拿切片做个去除字符串左右的空格
def trim(s):
        while s[:1]==' ':#如果0是空格  切记' '有空格！！！
                s=s[1:]#列表就从1开始  ，只要每次新列表的头一个有空格就一直循环
        while s[-1:]==' ':#如果最后一个是空格
                s=s[:-1]#列表就从0到倒数第二个， 只要每一次新列表的最后有空，就一直循环
        return s
print(trim('  sacc  '))
