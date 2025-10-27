# %%import datetime

print("Minimum and maximum", datetime.MINYEAR, datetime.MAXYEAR)

from datetime import timedelta
d1 = datetime.timedelta(days=1, hours=2, minutes=-30)
print(d1)

d2 = datetime.timedelta(days=-1, hours=-2, minutes=-3)
print(d2)

print("Timedelta sum:", d1+d2)
print("-----------------------------")

from datetime import date

print("Today is", datetime.date.today())
print("\n")

today = datetime.date.today()
daysToPay = datetime.timedelta(days=7)
print("Today is", today)
print("Bills should be paid within:", daysToPay.days, "days")
print("The bill should be paid till:", today + daysToPay)
print("\n")

endOfTheWorld = datetime.date.max
print("The final end of world will happen (by Python):", endOfTheWorld)
print(endOfTheWorld.weekday())
print("\n")

bornDate = datetime.date(1999,8,1)
today = datetime.date.today()
print(today - bornDate)
print("\n")
print("---------------------------")

from datetime import datetime

print("now()\t", datetime.now())
print("today()\t", datetime.today())
print("utcnow()\t", datetime.utcnow())
print("weekday()\t", datetime.today().weekday())
print("\n")

print("%a", datetime.now().strftime("%a"))
print("%A", datetime.now().strftime("%A"))
print("%w", datetime.now().strftime("%w"))
print("%a %A %w", datetime.now().strftime("%a %A %w"))
print("%Y-%m-%d_%H_%M_%S_%f", datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f"))


# %%
