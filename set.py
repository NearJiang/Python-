#set和dict类似，也是一组key的集合，但不存储value
s = set([1, 1, 2, 2, 3, 3])#set自动给过滤重复的
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)#重复部分
print(s1 | s2)#展示所有，有重复的就只显示一遍