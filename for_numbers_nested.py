# %%for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        #print(x, '*', y, '=', x*y)
        line += '\t%3d' % (x*y)
    print(line)

print('\n')

n=10
factorial = 1

for number in range(2,n+1):
    factorial *= number
    print(number,"! = ",number-1, '! *', number, '=', factorial)
    
print('\n')

n=10

for i in range(1,n+1):
    result = 1
    for j in range(1,i+1):
        result*=j
    print(i, result)
    
print('\n')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(adj , noun)
 
# %%
