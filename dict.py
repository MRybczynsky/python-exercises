CountryLeaders = {'PL':'Duda','US':'Trump'}

print(CountryLeaders)

print(CountryLeaders['US'])

CountryLeaders['DE'] = 'Scholz'

print(CountryLeaders.keys())
print(CountryLeaders.values())
print(CountryLeaders.items())
#print(CountryLeaders.popitem())
print(CountryLeaders.setdefault('FR', 'Macron'))
print(CountryLeaders.get('RU'))

NewLeaders = {'RU':'Putin', 'DE':'Schulz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders)
print(CountryLeaders)

chanels = {'Google':'1480', 'Email':'300', 'Natural Traffic':'440', 'TV Spot':'700'}
print(chanels['Email'])

chanelsUpdate = {'News':'600', 'Natural Traffic':'520'}
chanels.update(chanelsUpdate)

print(chanels.keys())

chanels.pop('Email')

print(chanels)
