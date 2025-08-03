# datetime module
import datetime
print(datetime)

# datetime class
from datetime import datetime
print(datetime)

# methods in datetime class now()-->to know th current time and date
print(datetime.now())

# strptime()-->standard format year,month,day
# Y-->Year
# y-->year
# m-->month
# d-->day
# B-->moth full name
# b-->month abb Name
# A-->week full Name
# a-->week abberivated
# M-->minutes
# S-->seconds
# H-->hours(24)
# I-->(12)
# p-->am or pm
print(datetime.strptime("29/07/2025","%d/%m/%Y"))

# strftime()-->change date and time to desire format
print(datetime.strptime("01/01/2020","%d/%m/%Y"))
now=datetime.now()
print(now.strftime("%b/%d/%y"))
print(now.strftime("%b/%d/%y %I/%M"))
print(now.strftime("%I/%M/%S"))
print(now.strftime("%I:%M:%S"))
print(now.strftime("%I:%M:%S:%A"))
print(now.strftime("%I:%M:%S:%a"))

# replace()-->replace date and time to desire format
print(now.replace(2024,12,12,20,50,45)) 
v=datetime.strptime("1999/11/11","%Y/%m/%d")
v=v.replace(1994-10-10)
print(v.strftime("%A"))

# weekday()-->return week day start from 0
print(datetime.now().weekday())

# isoweekday()-->return week day from 1
print(datetime.now().isoweekday())

# timedelta class-->return date after and before the mentioned date and time 
# parameters are week,day,hours,minutes,seconds,milliseconds,microseconds
# + denotes calculate after the date and time
# - calculate before the date and time
from datetime import datetime,timedelta
print(datetime.now()+ timedelta(days=100))
print(datetime.now()- timedelta(days=30,hours=20,seconds=50))

# time() date(): return particular time and date
print(datetime.now().date())
print(datetime.now().time())

# calculate the time between two given years or time
print((datetime.now()+timedelta(hours=100)).time())
