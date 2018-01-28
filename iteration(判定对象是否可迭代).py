Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from collections import Iterable
>>> isinstance(123,Iterable)
False
>>> isinstance([123],Iterable)
True
>>> isinstance([1,2,3],Iterable)
True
>>> isinstance('asdasd',Iterable)
True
>>> 
