dic = {'Near':99,'qibao':98,'k':85}#dict是{}，list是[]，tuple是()
print(dic['Near'])#但里面的是[]
dic['jie'] = 89 #字典名['']=x  就能通过key=value放入，一个key只对应一个value
print(dic)
dic.pop('k')#list里的pop()如果不加，就删除最后一个，dictionary不行，必须指定
#还有list的pop里是写数字，dictionary是写名字
print(dic)