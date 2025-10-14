# %%for number in range(1,21):
    if number%2 == 0:
        print('Number %2d is %s' % (number, 'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))

print('\n-------------------\n')

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for number in range(10):
    print(string_A)

print('\n-------------------\n')

for number in range(9):
    if number%2 == 1:
        print(string_A)
    else:
        print(string_B)

print('\n-------------------\n')

for number in range(9):
    print("x"*(number+1))

print('\n-------------------\n')

for number in range(9):
    if number % 2 == 0:
        print("o"*(number+1))
    else:
        print("x"*(number+1))
# %%
