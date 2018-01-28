#  在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象

import re

q = re.search(r'[1-9]\d{5}','QBB 100011 123155')
#如果匹配成功，返回一个Match对象，否则返回None
if q:#如果q匹配成功
    print(q.group(0)

        #只返回第一个match对象，要多个，得用finditer
