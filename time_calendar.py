# %%#time
import time
print("Current time is... unix epoch", time.time())
print("\n")
print("Current time is... tuple", time.localtime(time.time()))
print("\n")
print("Current time is... for human", time.asctime(time.localtime(time.time())))
print("\n")
print("Current time is... for human", time.localtime(time.time()))
print("\n\n\n")

#calendar
import calendar
print("--------------------------------")
print(calendar.month(2017,9,w=5,l=2))
print("--------------------------------")
print(calendar.month(2017,9))
print("--------------------------------")
print("week day is",calendar.weekday(2017,9,29))
print("--------------------------------")
calendar.setfirstweekday(6)
print("--------------------------------")
print(calendar.month(2017,9))
print("--------------------------------")
print("week day is",calendar.weekday(2017,9,29))
print("--------------------------------")
print("is 2000 a leap year",calendar.isleap(2020))
print("--------------------------------")
print("Leap days 2000-2017", calendar.leapdays(2000,2017))
print("Leap days 2000-2020", calendar.leapdays(2000,2020))
print("Leap days 2000-2021", calendar.leapdays(2000,2021))

print(calendar.calendar(2018))

# %%
