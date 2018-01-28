#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

#如果要保持Key的顺序，可以用OrderedDict

>>> from collections import OrderedDict
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])#tuple list tuple
>>> d
{'a': 1, 'b': 2, 'c': 3}#说dict Key是无序的，在我这还从来没出现过无序。。。
>>> q=OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> q
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> 
>>> 
>>> j = OrderedDict()
>>> j['z']=1
>>> j['y']=1
>>> j['x']=1
>>> j
OrderedDict([('z', 1), ('y', 1), ('x', 1)])#按照插入顺序排

#OrderedDict可以实现一个FIFO（先进先出）的dict，
#当容量超出限制时，先删除最早添加的Key
#First Input First Output

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
