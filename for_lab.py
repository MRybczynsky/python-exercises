# %%fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0

for i in range(0,20):
    print('Step', i+1, 'value',a3)
    a1=a2
    a2=a3
    a3=a1+a2

print("----------------------------------------")

text = '''Industrial Light & Magic" is a company famous for pioneering visual effects in film,
founded by George Lucas in 1975. The name originated from a warehouse location zoned 
for "light industrial" and the idea of creating "magic" with light and technology, as explained by Lucas.
The phrase describes their innovative and groundbreaking work, which includes creating stunning digital 
and practical effects for hundreds of movies and shows.'''

listOfWords = text.replace('\n', ' ').replace('"','').replace('&', '').replace(',', '').replace('.', '').split(' ')

for word in listOfWords:
        if "p" in word.lower():
            print(word)

print("----------------------------------------")

dictionary = {'A':'80%-100%','B':'60%-80%','C':'50%-60%','D':'less than 50%'}

for key, value in dictionary.items():
    print(f"{key} - {value}")

print("----------------------------------------")

wordDictionary = {}
for word in listOfWords:
    if word in wordDictionary.keys():
        wordDictionary[word] += 1
    else:
        wordDictionary[word] = 1

print(wordDictionary)
# %%
