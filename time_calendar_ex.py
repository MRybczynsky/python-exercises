# %%import time

print("Current time is... unix epoch", time.time())
print("\n")
print("Current time is... tuple", time.localtime(time.time()))
print("\n\n\n")

import calendar
print("Important month: \n", calendar.month(2016,9))
calendar.setfirstweekday(6)
print("Important month: \n", calendar.month(2016,9))
print("\n")
print("Is 2000 leap: ", calendar.isleap(2000))
print("\n")
print(calendar.calendar(2019))
# %%
