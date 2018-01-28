# 在一个字符串中替换所有匹配正则表达式的字串，返回替换后的字符串

import re

q = re.sub(r'[1-9]\d{5}',':yyy','QBB100011 JBB159357')
print(q)

q = re.sub(r'[1-9]\d{5}',':yyy','QBB100011 JBB159357',1)#count默认为0，功能同maxsplit
print(q)

