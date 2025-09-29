isAutomaticMode = True

is80PercentLight = True

isDirectLight = False

isRainy = True

turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)

print("Automatic mode: ", isAutomaticMode)
print("Is the light good: ", is80PercentLight)
print("Is sun low: ", isDirectLight)
print("Is it rainy: ", isRainy)
print("TURN LIGHTS ON: ", turnLightsOn)


v1 = 126
v2 = '126'
v3 = 126.0
v4 = '126.0'
print ('V1 to: ', type(v1))
print ('V2 to: ', type(v2))
print ('V3 to: ', type(v3))
print ('V4 to: ', type(v4))

'''wynik dodawania v1 i v3 oraz typ tak wyznaczonego wyniku
wynik dodawania v2 i v4 oraz typ tak wyznaczonego wyniku'''

suma1 = v1+v3
print ('v1 + v3 = ', suma1, type(suma1))

suma2 = v2+v4
print ('v2 + v4 = ', suma2, type(suma2))

wynik1 = 7-1*0+3+3
print('7-1*0+3+3 = ', wynik1 )

#Ile to jest  4 do potęgi piątej podzielone przez 2 do potęgi 3

wynik2 = (4**5)/(2**3)
print('(4**5)/(2**3) = ', wynik2 )

wynik3 = 9
print('Wynik łamigówki to: ', wynik3)
