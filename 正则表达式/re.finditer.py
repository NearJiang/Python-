# 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象

import re

for q in re.finditer(r'[1-9]\d{5}','QBB100011 JBB159357'):
    if q:
        print(q.group(0))


