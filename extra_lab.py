# %%initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year = 0
capital = initialCapital

while year<maxTimeYears:
    capital = round((1+percent)*capital,2)
    print("After this year: ", year, 'you will have:', capital)
    year +=1
else:
    print("The total revenue is", capital-initialCapital)

print("------------------------------------------------")

number = 20730906
tmpNumber = number
sumOfDigits = 0

while tmpNumber > 0:
    digit = tmpNumber%10
    sumOfDigits +=digit
    tmpNumber = tmpNumber//10
else:
    print("The sum of digits of", number, "is", sumOfDigits)


print("------------------------------------------------")

text= '''The company United Space Alliance was a major support contractor for NASA,
specifically for the Space Shuttle program. Formed as a joint venture between 
Rockwell International and Lockheed Martin, it was the single prime contractor 
for NASA's Space Flight Operations Contract and managed the Space Shuttle fleet 
and the International Space Station from 1996 until operations ceased. '''

wordLength = 6

listOfWords = text.replace('\n', ' ').split(' ')

shortWords = 0
longWords = 0
i = 0

while i<len(listOfWords):
    if len(listOfWords[i])>wordLength:
        longWords+=1
    else:
        shortWords+=1
    i+=1


print("Words shorter than ", wordLength, ":", shortWords)
print("Words longer than ", wordLength, ":", longWords)
# %%
# %%
