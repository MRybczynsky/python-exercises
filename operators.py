IsWeekend = False
print("Is weekend = ", IsWeekend)

Temperature = 5
print("Temperature = ", Temperature)

ToDoList = 'Shopping'
print("ToDoList = ", ToDoList)

IsHappy = IsWeekend and Temperature >=20 and ToDoList == ''
print("Is Happy = ", IsHappy)

IsHappy = not IsWeekend and Temperature <20 and ToDoList != ''
print("Is Happy = ", IsHappy)
