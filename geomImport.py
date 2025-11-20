# %%import geom

print(geom.GiveGeomSeqElement(1,2,64), '\n')

a1=3
factor=2
maxindex = 11

for i in range(1,maxindex+1):
    print('a',i,'=',geom.GiveGeomSeqElement(a1,factor,i))

print('\nFactor is', geom.GiveFactorForGeomSeq(12,24), '\n')

print('Sum of n elements is', geom.GiveSumOfNElementsGeomSeq(2,3,4))
# %%
