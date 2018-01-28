>>> from datetime import datetime, timedelta, timezone
>>> now = datetime.utcnow()#世界标准时间
>>> print(now)
2018-01-13 13:20:23.860909
>>> q=now.replace(tzinfo=timezone.utc)#强制设置时区为UTC+0：00：
>>> print(q)
2018-01-13 13:20:23.860909+00:00
>>> China=q.astimezone(timezone(timedelta(hours=8))) #astimezone
>>> print(China)
2018-01-13 21:20:23.860909+08:00
>>> JP=q.astimezone(timezone(timedelta(hours=9)))
>>> print(JP)
2018-01-13 22:20:23.860909+09:00
>>> 
>>> JP2=China.astimezone(timezone(timedelta(hours=9)))
>>> print(JP2)
2018-01-13 22:20:23.860909+09:00
>>> 

#不是必须从UTC+0:00时区转换到其他时区，
#任何带时区的datetime都可以正确转换，
#例如上述China到JP的转换


#强制设置为UTC+8:00
>>> now = datetime.now()
>>> q=now.replace(tzinfo=timezone(timedelta(hours=8)))
>>> print(q)
2018-01-13 21:33:06.204298+08:00
