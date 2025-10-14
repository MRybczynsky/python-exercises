# %%number = 1
previousNumber = 0

while(number<50):
    print("Sum: ", number + previousNumber)
    previousNumber = number
    number+=1
    
##########################

import random

my_number = random.randint(0,20)
guess = -1
trials = 1
print("Guess my number!")

while (my_number != guess):
    guess = int(input())
    if(my_number == guess):
        print("Congrats! Number of your trials: ", trials)
    else:
        print("Sorry - my number is greater than your guess... try again")
        trials+=1


# %%
