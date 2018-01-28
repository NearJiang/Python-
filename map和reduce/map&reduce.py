#字符串str也是一个序列，对上面的例子稍加改动，配合map()，
#我们就可以写出把str转换为int的函数
from functools import reduce
def trans(x,y):
    return x*10+y

#字符型(char)
def char_num(j):
    digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[j]

print(reduce(trans,map(char_num,'13579')))

#整理出  str_int:
from functools import reduce

digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str_int(j):
    def trans(x,y):
        return x*10+y
    def char_num(j):
        return digits[j]
    return reduce(trans,map(char_num,j))
print(str_int('156165'))

#lambda进一步简化:
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char_num(j):
    return DIGITS[j]
def str_int(j):
    return reduce(lambda x,y:x*10+y,map(char_num,'j'))#lambda直接在函数运用中定义
print('7899465')
