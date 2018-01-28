Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> q = re.search(r'[1-9]\d{5}','QBB 100011 123155')
>>> q.string# 待匹配的文本
'QBB 100011 123155'
>>> q.re#正则表达式
re.compile('[1-9]\\d{5}')
>>> q.pos#搜索的起始位置
0
>>> q.endpos#搜索的结束位置
17
>>> q.group(0)#匹配后的字符串，只能得到一个，要多个，用finditer
'100011'

>>> q.start()#匹配的字符串 的头部位置
4
>>> q.end()#匹配的字符串 的尾部位置
10
>>> q.span()#匹配的字符串 的头尾位置
(4, 10)
>>> 
