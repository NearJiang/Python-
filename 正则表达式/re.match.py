#  从一个字符串的开始位置起匹配正则表达式，返回match对象

import re
q = re.search(r'[1-9]\d{5}','100011 QBB')

if q:
    print(q.group(0))
