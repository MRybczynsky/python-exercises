sthLikeNum = '1000'
print(sthLikeNum)

print(int(sthLikeNum) + 1)

print(sthLikeNum + str(1))

print(type(sthLikeNum))
print(type(int(sthLikeNum) + 1))


article = '''This article is about the comedy group.
For their TV show frequently called Monty Python,
see Monty Python's Flying Circus.
"Pythonesque" redirects here.
For the play by Roy Smiles, see Pythonesque (play).
"The Pythons" redirects here.
For the documentary film about the group, see The Pythons (film).'''

print(article.upper())
print('\n')
print(article.lower().replace('monty', 'flying'))
print('\n')
print(article.split(' '))

#word python appears 6 times
print('\n')
print('word python appears ', article.lower().count('python'), ' times')

print('\nThe best hits of \'80s!!!')
print("\nThe best hits of \'80s!!!")

'''
cur   exchange amount
USD   3.65     64.10958904109589
EUR   4.23     55.31914893617021 '''

amountPLN = 234

print('cur', 'exchange', 'amount', sep = '\t')
print('USD', '3.65', amountPLN/3.65, sep = '\t')
print('EUR', '4.23', amountPLN/4.23, sep = '\t')

ValueAsText = '123.45'
factor = 1.23

#value is  123.45 factor is 1.23 value*factor= 151.8435

print('\nvalue is ' + ValueAsText + ' factor is ' + str(factor) + ' value*factor = ' + str(float(ValueAsText)*factor))




