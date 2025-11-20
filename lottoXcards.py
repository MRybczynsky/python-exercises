# %%import random

myNumbers = []

while len(myNumbers) < 7:
    newNumber = random.randint(1,49)
    if newNumber in myNumbers:
        print("Eliminated: ", newNumber)
        continue
    myNumbers.append(newNumber)

print("Those number will win: ", myNumbers)

print("--------------------------------")

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []

for color in colors:
    for figure in figures:
        newCard = color + ' ' + figure
        allCards.append(newCard)

print("All cards: ", allCards)

random.shuffle(allCards)

print("\nAll cards after shuffle: ", allCards)

player1 = []
player2 = []
maxi = len(allCards)
i=0

while i < maxi-1:
    if i%2==0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
    i+=1

print("\nPlayer 1: " , player1)
print("\nPlayer 2: " , player2)

player1 = allCards[:12]
player2 = allCards[12:]
 
print("\nPlayer 1: " , player1)
print("\nPlayer 2: " , player2) 

# %%
# %%
