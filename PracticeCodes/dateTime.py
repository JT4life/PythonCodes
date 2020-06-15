#Python date, time, datetime class
#Date and datetime, are objects in python
#5 main classes: date (manipulate date(month,d,year)
#           time (independent of the day : hour,min,secs,mil secs)
#           datetime (combination of both)
#           timedelta (duration of time use for manipulation of dates)
#           tzinfo (Abstract class dealing with timezone)

'''import time
a = time.localtime()
print(a)
print(time.asctime(a))
a=time.asctime(time.localtime(time.time()))
print(a)

time.sleep(10)#sleep for 10 seconds
a = time.localtime()
print(time.asctime(a))'''

'''from datetime import date
from datetime import time
from datetime import datetime
def main():
    today=datetime.now();
    print(today)

    t=datetime.time(datetime.now())
    print(t)

    wd=date.weekday(today)
    print(wd)

    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print(days[wd])

if __name__=="__main__":
    main()'''

'''#Timedelta object : We can estimate the time for past and future
#or we can say its a timespan

from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import date

print(timedelta(days=365,hours=8,minutes=15))
print("Today is:"+str(datetime.now()))
print("One Year from now is:"+str(datetime.now()+timedelta(days=365)))
print("One Week and 4 days from now is:"+str(datetime.now()+timedelta(weeks=1,days=4)))

#How many days until new years day?
today=date.today()
nyd=date(today.year,1,1)
print((today-nyd).days)'''

'''#Python calendar

import calendar
c=calendar.TextCalendar(calendar.MONDAY)
str=c.formatmonth(2019,1)
print(str)

c=calendar.HTMLCalendar(calendar.MONDAY)
str=c.formatmonth(2019,1)
print(str)

print(calendar.month(2019,4))
print(calendar.prcal(2020))'''


