# %%from datetime import date

def daysToNewYearEve(year=date.today().year,
                   month=date.today().month,
                   day=date.today().day):
    # date_today = date.today()
    # current_year = date_today.year
    date_end_year = date(year,12,31)
    delta = date_end_year - date(year,month,day)
    #print(delta.days)
    return delta.days

def daysToNewYearEve2(*da_te):
    for d in da_te:
        date_end_year = date(d.year,12,31)
        delta = date_end_year - d
        print('Date',d,'days to end of year',delta.days)
    return

print(daysToNewYearEve(2025,11,1))
print(daysToNewYearEve())
daysToNewYearEve2(date(2025,11,1))
daysToNewYearEve2(date(2025,11,2),date(2025,10,2),date(2025,9,12))

    

# %%
