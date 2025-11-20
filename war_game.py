# %%import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]
allCards = []

for color in colors:
    for figure in figures:
        aCard = figure.copy()
        aCard['Color'] = color
        allCards.append(aCard)

#print("All cards: ", allCards)

random.shuffle(allCards)

#print("\nAll cards after shuffle: ", allCards)

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

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1['Power'] == card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card2)
        player2.append(card1)
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
 
if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')



        
# %%
