#排序
print(sorted([36, 5, -12, 9, -21]))

#接受一个key函数实现自定义排序，例如abs绝对值
print(sorted([36, 5, -12, 9, -21], key=abs))

#字符串排序,默认按ASCII(0:48 9:57/ A：65-Z：90/ a:97 z:122 )
#就是说如果字符串，里面的数字排在首位，然后是大写字母，然后是小写字母
print(sorted(['bob', 'about', 'Zoo', 'Credit','1']))

#我们现在要忽略大小写，也就是让所有字符串变成大写或者小写  再比较
print(sorted(['bob', 'about', 'Zoo', 'Credit','5'], key=str.upper))

#结果反过来，so easy  我们的reverse出场！！  不写true可是不行的!!
print(sorted(['bob', 'about', 'Zoo', 'Credit','5'], key=str.upper,reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=lambda x:x[0]))
#把('Bob', 75)代入lambda，return它的第一个元素Bob，其他名字一样，
#最后得到Bob,Adam,Bart,Lisa
#默认根据ASCII,就是A B B L,相同字母会再根据后面的字母比较
print(sorted(L,key=lambda x:x[0],reverse=True))

#把('Bob', 75)代入lambda，return它的第2个元素75
#最后得到75，92，66，88
#默认从小到大
print(sorted(L,key=lambda x:x[1]))
print(sorted(L,key=lambda x:x[1],reverse=True))
#75输入 return - 75，最后就是-75，-92，-66，-88
#默认从小到大，-92，-88，-75，-66
#对应的就是92，88，75，66  
print(sorted(L,key=lambda x:-x[1]))

#说不清了，脑子转不过来，就reverse=True就好了，哪这么多废话
