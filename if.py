age = 23
isDrunk = False
isRestrictedArea = False

if age >= 18 and not isDrunk and not isRestrictedArea:
    print("You are adult and you can buy alcohol")
else:
    print("You can't buy alcohol")

likes = 510
shares = 10

if likes >= 500 and shares >=100:
    print("Discount 10%")
else:
    print("No discount")

if age < 18:
    print("You are too young")
elif isDrunk:
    print("Are you drunk?")
elif isRestrictedArea:
    print("Restricted area")
else:
    print("Ok")

if likes < 500:
    print("Not enought likes")
else:
    if shares < 100:
        print("Not enought shares")
    else: 
        print("Discount 10%")

if likes >=500 and shares >=100:
    print("Discount 10%")
elif likes < 500:
    print("Not enought likes")
else:
    print("Not enought shares")


pizza = True
bigDrink = False
noWeekend = False

if (pizza or bigDrink) and noWeekend:
    print("Burger bon!")
elif noWeekend == False:
    print("It's weekend")
else:
    print("You didn't buy pizza or big drink")


