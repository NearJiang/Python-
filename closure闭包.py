#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

def lazy_sum(*args):
    def sum():
        math=0
        for i in args:
            math=math + i
        return math
    return sum

#当我们调用lazy_sum的时候，调用的是里面的求和函数，return sum，而不是求和结束
q = lazy_sum(1,3,5,8,9)
#直接print(q)是没用的
print(q())


#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
