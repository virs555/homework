from datetime import datetime, timedelta

dt_now = datetime.now()
dt_delta1 = timedelta(days=1)
dt_delta30 = timedelta(days=30)
print(dt_now - dt_delta1)
print(dt_now)
print(dt_now - dt_delta30)

date_string = '01/01/25 12:10:03.234567'
date_string = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_string)