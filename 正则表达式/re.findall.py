#  搜索字符串，以列表类型返回全部能匹配的子串


import re
q = re.findall(r'[1-9]\d{5}','100011QBB JBB555666')#加个[0]看看
print(q)
