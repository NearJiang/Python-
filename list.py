classmates = ['Near', 'Bob', 123,[True,'jump'],'Tracy']
print(classmates[3][1])
classmates.append('Adam')#append 加在最后
classmates.insert(1, 'Jack')#insert随你插，之后的数就都+1，记住0是第一个
classmates[1] = 'Sarah'#覆盖原来的，直接替换了
classmates.pop()#就是删除最后一个
classmates.pop(0)#删除你指定的
print(classmates)#不能加‘’，因为classmates是个list，加‘’就是个字符串了
print(len(classmates))#list中的个数
print(classmates[0])
print(classmates[-1])#-1就是最后一个

