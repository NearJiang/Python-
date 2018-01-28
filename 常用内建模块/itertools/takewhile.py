import itertools

natuals = itertools.count(5)
q = itertools.takewhile(lambda x : x<=10,natuals)

print(list(q))


#无限序列虽然可以无限迭代下去，
#但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
