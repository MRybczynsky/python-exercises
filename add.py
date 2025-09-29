''' 1. W tym zadaniu możesz się spodziewać ciekawego wyniku. (jeżeli chcesz sprawdzić
jego działanie w innym roku niż 2017 to zmień liczbę 1017, np dla roku bieżącego 2019 należy użyć 1019):

>>> Zapisz swój numer buta i pomnóż przez 5. Do tego dodaj 50. Całość pomnóż przez 20,
a następnie dodaj 1017. Odejmij od tego swój rok urodzenia. Wyszła 4cyfrowa liczba. Pierwsze dwie cyfry
to Twój numer buta a dwie ostatnie to Twój wiek.<<<

2. Kolejne działanie z tego samego cyklu:

>>>Pomyśl liczbę nieujemną całkowitą. Pomnóż ją przez 2, dodaj 10, podziel przez 2, odejmnij początkową liczbę.
Powinno wyjść 5 - zawsze. <<<

3. Ile to jest - najpierw policz sam, a potem sprawdź rozwiązanie pythona

2+2*2 = ?

7+7/7+7*7-7 = ?

4. Wykładowca mówi studentom. Zaliczysz semestr jeżeli masz obecność co najmniej 80%
i średnią >= 3.0 lub zaliczyłeś pracę semestralną. Zbuduj wyrażenie w Python które stwierdzi czy student,
który ma obecność 0.85, średnią 3.5 i nie zaliczył pracy semestralnej zda czy nie.

5. Wykładowca zmienił zdanie. Aby zaliczyć semest trzeba: mieć obecność co najmniej 80%, średnią >=3.0
i zaliczoną pracę. Czy teraz student zda?

6. Zmieniamy dane studenta. Teraz ma obecność 40%. średnią 2.5 ale zaliczył pracę semestralną.
Sprawdź wg którego z kryterów student zaliczy semestr.

 '''

result = (42*5+50)*20+1025-1999
print(result)

result2 = (7*2+10)/2-7
print(result2)

result3 = 2+2*2
print(result3)

result4 = 7+ 7/7 +7*7-7
print(result4)

obecnosc = 0.4
srednia = 2.5
praca = True

zdane = (obecnosc >= 0.8 and srednia >= 3)or praca
print("Zdane: ", zdane)

zdane2 = obecnosc >= 0.8 and srednia >= 3 and praca
print("Zdane: ", zdane2)
