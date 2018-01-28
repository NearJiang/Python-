如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，
接下来重复使用时就不需要编译这个步骤了，直接匹配

>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')#compile：编译 re.complie
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
