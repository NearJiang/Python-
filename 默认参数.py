#：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给
#参数x和n
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
#这个时候，默认参数就排上用场了
#这样，当我们调用power(5)时，相当于调用power(5, 2)
#不写n就默认是平方，你要立方各种几次方那就可以正常抒写（5，3）
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#必选参数在前，默认参数在后

#变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
#以上面为例，x每个人脑里可以想各种数，后面几次方，绝大部分人平方想的还是很多的

def enroll(name, gender, age=6, city='Beijing'):#只要您孩子6岁
    print('name:', name)    #是我们正宗北京人儿
    print('gender:', gender)#那您这入学表填个名字跟性别就行奈您
    print('age:', age)#要是6岁，但不是这北京人儿，麻烦您还得写个你哪儿的
    print('city:', city)#要是是咱们这个北京人儿，但不是这6岁，还得您写个岁数
 #有多个默认参数时，调用的时候
print(enroll('Bob', 'M', 7))#按顺序提供默认参数，这个7就不要写age=
print(enroll('Adam', 'M', city='Tianjin'))
#不按顺序提供部分默认参数时，需要把参数名写上
#def不写return就返回个none

#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
def add_end(L=[]):#传入一个list
    L.append('END')
    return L
>>> add_end([1, 2, 3])
[1, 2, 3, 'END']
>>> add_end()#当你使用默认参数调用时，一开始结果也是对的：
['END']
>>> add_end()#再次调用add_end()时，结果就不对了：
['END', 'END']
>>> add_end()
['END', 'END', 'END']
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
#则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
