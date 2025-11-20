# %%def weekDayInFrench(dayNumber):
    names = {
        0: 'Lundi',
        1: 'Mardi',
        2: 'Mercredi',
        3: 'Jeudi',
        4: 'Vendredi',
        5: 'Samedi',
        6: 'Dimanche' 
        }
    return names.get(dayNumber,'error')

print(weekDayInFrench(4))
# %%
