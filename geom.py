# %%import math

def GiveGeomSeqElement(a1=2,factor=2,index=2):
    result = a1*pow(factor,index-1)
    return int(result)

def GiveFactorForGeomSeq(term, nextterm):
    return nextterm/term

def GiveSumOfNElementsGeomSeq(a1=2,factor=2,n=2):
    sumN = a1*(1-pow(factor,n))/(1-factor)
    return sumN
