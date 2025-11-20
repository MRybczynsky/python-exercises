# %%from datetime import date

def giveWorkingDay(year=date.today().year,
                   month=date.today().month,
                   day=date.today().day):
    from datetime import date
    from datetime import timedelta

    #day = date.today()
    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    #print('workind day for', day, 'is', workingday)

    return workingday


nextWorkingDay = giveWorkingDay(2017,9,2)
print('Next workind day after', 2017,9,2, 'is', nextWorkingDay)
nextWorkingDay = giveWorkingDay()
print('Next workind day after today is', nextWorkingDay)
print('Next workind day after today is', giveWorkingDay())

# %%
