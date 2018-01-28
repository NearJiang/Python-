>>> from datetime import datetime, timedelta
>>> now = datetime.now()
>>> now
datetime.datetime(2018, 1, 13, 21, 1, 1, 590097)

>>> now + timedelta(hours=10)
datetime.datetime(2018, 1, 14, 7, 1, 1, 590097)

>>> now + timedelta(days=1,hours=10)
datetime.datetime(2018, 1, 15, 7, 1, 1, 590097)

>>> now - timedelta(days=1,hours=10)
datetime.datetime(2018, 1, 12, 11, 1, 1, 590097)
>>> 
