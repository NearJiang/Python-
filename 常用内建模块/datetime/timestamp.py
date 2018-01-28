timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00#世界标准时间

              = 1970-1-1 08:00:00 UTC+8:00#对应的北京时间 +8
              
>>> from datetime import datetime
>>> publish = datetime(2018,1,1,22,15)
>>> publish.timestamp()
1514816100.0
>>> 
>>> q=1514816100.0
>>> print(datetime.fromtimestamp(q))
2018-01-01 22:15:00
#timestamp和本地时间做转换（你电脑设置的时区）
>>> print(datetime.utcfromtimestamp(q))#加个utc就是返回世界标准时间
2018-01-01 14:15:00
