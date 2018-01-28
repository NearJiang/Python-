import itertools

natuals = itertools.count(2)#从几开始，count()会创建一个无限的迭代器，只能ctrl+c

for n in natuals:
    print(n)
