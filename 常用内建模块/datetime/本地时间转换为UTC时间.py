>>> from datetime import datetime, timedelta, timezone
>>> tz_utc_9 = timezone(timedelta(hours=9))
>>> now=datetime.now()

>>> now
datetime.datetime(2018, 1, 13, 21, 9, 39, 774802)
>>> q=now.replace(tzinfo=tz_utc_9)
>>> q
datetime.datetime(2018, 1, 13, 21, 9, 39, 774802,
                  tzinfo=datetime.timezone(datetime.timedelta(0, 32400)))
#没明白
