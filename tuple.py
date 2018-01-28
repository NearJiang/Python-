#tuple和list类似，但没有append，insert这样的增插删功能。

#list是[],tuple是()

#1个元素的tuple定义时必须加一个逗号,，来消除歧义 t = (1,),写

classmates = ('Michael', 'Bob', 'Tracy',['A', 'B'])

classmates[3][0] = 'X'#啊啊啊啊，你才说的tuple是不可变的，这么快就变心了！！渣男！
classmates[3][1] = 'Y'#stop，这边我们改的是什么？是tuple里的list啊，对不对！
print(classmates[-1])