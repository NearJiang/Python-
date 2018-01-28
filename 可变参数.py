def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#上面number是个常量参数，我们调用的时候得用个list或tuple
>>> calc([1, 2, 3])
14

def calc(*numbers):#我们把参数改成可变参数 *numbers
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#函数内部，参数numbers接收到的是一个tuple，所有调用函数时，就可简化成以下：

>>> calc(1, 2)


#如果已经有一个list或者tuple：
nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])#但这样太麻烦

>>> calc(*nums)#自动组装成calc（1，2，3）

#可变参数允许你传入0个或任意个参数！！！！！
#这些可变参数在函数调用时自动组装为一个tuple！！！！
