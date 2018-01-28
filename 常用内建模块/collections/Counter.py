>>> from collections import Counter
>>> c = Counter()
>>> for char in 'programming':
...     c[char]+=1 #counter计数器默认计数一个为0，所以c[char]+=1
...
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
