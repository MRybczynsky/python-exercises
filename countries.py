countries = ['FR', 'US', 'DE', 'RU']
print(countries)
print(countries[1])
countries[1] = 'GB'
print(countries)
countries.append('PL')
countries.insert(2, 'ES')
countries.remove('RU')
countries.sort()
countries.reverse()
#wywolanie + usuniecie z listy
print(countries.pop(2))
print(countries.index('PL'))
print(countries.count('DE'))

newList = ['FI', 'SE']
countries.extend(newList)

countriesCopy = countries.copy()
countriesCopy.clear()


print(countries)
print(countriesCopy)
