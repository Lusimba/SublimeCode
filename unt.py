import time
import datetime
import pytz
import calendar
# z = calendar.month(2018, 12)
# print (dir(calendar))

x = datetime.datetime.now()
y = datetime.timedelta(hours = 11)
print (x, " ,", x+y)


# dt

# for tz in pytz.all_timezones:
#     print(tz)