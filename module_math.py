# %%f_smaller = 3.141592653589793 
f_bigger = 3.87756392764

print(f_smaller, f_bigger)
print("\n")

print(int(f_smaller), int(f_bigger))
print("\n")

print(abs(f_smaller), abs(-f_bigger))
print("\n")

print(round(f_smaller,2), round(f_bigger,2), round(f_bigger,3))
print("\n")

print(min(f_smaller, f_bigger), max(f_smaller, f_bigger))
print("\n")

list = [1,2,3,4,5,6,7,8,9]

print(max(list))
print("\n")

print(sum(list), len(list))
print("\n")

print(sum(list)/len(list))
print("\n")

print(round(2.675, 2))
print("\n")

import math

print(math.ceil(f_smaller), math.ceil(f_bigger))
print("\n")

print(math.floor(f_smaller), math.floor(f_bigger))
print("\n")

print(math.ceil(-f_smaller), math.ceil(-f_bigger))
print("\n")

print(math.floor(-f_smaller), math.floor(-f_bigger))
print("\n")

print(pow(2,8),pow(9,0.5))
print("\n")

print(math.sqrt(16))
print("\n")

print(math.pi, math.e)
print("\n")

print(math.sin(math.pi/2), math.cos(math.pi/4))
print("\n")

percent = [2.606255012,1.222935044,1.283079391,3.628708901, 6.856455493,4.911788292,
2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
8.740978348,6.174819567]

countries = ['Ukraine', 'Spain','Slovenia', 'Lithuania','Austria','Estonia','Norway','Portugal','United Kingdom',
'Serbia','Germany','Albania','France', 'Czech Republic','Denmark', 'Australia', 'Finland','Bulgaria',
'Moldova','Sweden','Hungary', 'Israel','Netherlands','Ireland','Cyprus', 'Italy']

sumOfPoints = 4988

print('Min: ', min(percent))
print('Max: ', max(percent))


for i in range(len(countries)):
    print(countries[i] , ':' , percent[i], ';', int(percent[i]), ';', round(percent[i],2), ';', int(round(percent[i]*sumOfPoints/100,0)))

print('--------------------------------')

import statistics

percent.sort()

print(statistics.median(percent))
print(statistics.median_low(percent))
print(statistics.median_high(percent))

from statistics import *

median(percent)

# %%
