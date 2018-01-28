#str转换为datetime
>>> from datetime import datetime
>>> q = datetime.strptime('2018-1-1 23:59:59','%Y-%m-%d %H:%M:%S')
>>> print(q)    #strp 
2018-01-01 23:59:59#datatime标准形式，月份是个数，前面有0
>>> 
#datetime转换为str
>>> now=datetime.now()
>>> print(now)
2018-01-13 20:51:51.126779
>>> print(now.strftime('%a,%b %d %H:%M'))#strf
Sat,Jan 13 20:51

#Y year
#m month
#d day

#H hour
#M minute
#S second

#a 星期几
#b 月份

