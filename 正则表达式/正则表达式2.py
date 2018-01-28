#要做更精确地匹配，可以用[]表示范围
[0-9a-zA-Z\_]可以匹配一个数字 字母或者_下划线

[0-9a-zA-Z\_]+   可以匹配至少由一个数字、字母或者下划线组成的字符串，
                 比如'a100'，'0_Z'，'Py3000'等等

[a-zA-Z\_][0-9a-zA-Z\_]*
可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}
字母或下划线开头
后面最多19个字符
PY[TH]ON:  PYTON,  PYHON
# [^]表示排除,[^abc]:不能出现a，b，c

#A|B可以匹配A或B  abc|def：abc或def
(P|python)可以匹配到'Python'或'python'

# ^表示行的开头，^\d表示必须以数字开头  ^读法：caret

# [^]表示排除,[^abc]:不能出现a，b，c

#  $表示行的结束，\d$表示必须以数字结束


py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了

判断正则表达式是否匹配：
>>> import re
>>> re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>

match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None

常见的判断方法就是：

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
