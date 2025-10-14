# %%import random
print("One random number:", random.randint(1,100))
print("\n")

print("One random number from a range", random.choice(range(1,100)))
print("\n")

print("One random number from a range - easier", random.randrange(1,100))
print("\n")

list = ['John', 'Ann', 'Peter', 'Susan', 'Emily', 'Greg', 'Chris']
random.shuffle(list)
print("Reordered list: ", list)
print("\n")

print("Just a random float", random.random())
print("\n")

print("--------------------------------")

toto = []
for i in range(10):
    toto.append(random.randrange(1,100))

print(toto)
print("--------------------------------")

number1 = random.randrange(1,100)
number2 = 0
counter = 0

while (number1!=number2):
    number2 = random.randrange(1,100)
    counter +=1
else:
    print("Number1 == Number2 = ", number1, "Number of attempts: ", counter)

print("--------------------------------")

countries = ['Ukraine', 'Spain','Slovenia', 'Lithuania','Austria','Estonia','Norway','Portugal','United Kingdom',
'Serbia','Germany','Albania','France', 'Czech Republic','Denmark', 'Australia', 'Finland','Bulgaria',
'Moldova','Sweden','Hungary', 'Israel','Netherlands','Ireland','Cyprus', 'Italy']

random.shuffle(countries)

groupNumber = 0

for i in range(len(countries)):
    if(i%4==0):
        groupNumber += 1
        print("---Group %d---" % (groupNumber))
    print(countries[i])
        
    
# %%
# %%
# %%
