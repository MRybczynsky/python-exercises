# %%import math

def GiveGeomSeqElement(a1=2,factor=2,index=2):
    result = a1*pow(factor,index-1)
    return int(result)

print(GiveGeomSeqElement())
print(GiveGeomSeqElement(1,2,64), '\n')

a1=3
factor=2
maxindex = 10

for i in range(1,maxindex):
    print('a',i,'=',GiveGeomSeqElement(a1,factor,i))

def GiveFactorForGeomSeq(term, nextterm):
    return nextterm/term

print('\nFactor is', GiveFactorForGeomSeq(12,24), '\n')

def GiveSumOfNElementsGeomSeq(a1=2,factor=2,n=2):
    sumN = a1*(1-pow(factor,n))/(1-factor)
    return sumN
print('Sum of n elements is', GiveSumOfNElementsGeomSeq(2,3,4))

    
# %%
# %%
