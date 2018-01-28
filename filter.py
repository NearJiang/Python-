#filter,和map类似，也接受一个函数和一个序列
#把传入的函数依次作用于每个元素，根据返回值是True还是False决定保留还是丢弃

#保留奇数，过滤掉偶数
def must_odd(n):
    return n % 2 == 1

print(list(filter(must_odd,[1,2,3,4,5,6,7,8,9])
    )
    )
#1%2 的意思是求1除以2得到的余数,而1除以2 = 0 余1 所以 1%2是1
#把list中的元素代入must_odd中，1，3，5，7，9  %2都余1，返回值为True，保留
#2，4，6，8 %2余0，返回值为Fales，丢弃

#去掉空字符串
def not_empty(q):
    return q and q.strip()
#经过q and q.strip()还有值的就返回True，是空的字符串的就就False
print(list(filter(not_empty,['A','b','','   ',None,'  jiang'])
    )
    )
