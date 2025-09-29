Tax = (4,7,8,23)

print(Tax)

print(Tax[-1])

print(Tax.index(7))

print(Tax.count(8))

print(max(Tax))

TaxList = list(Tax)
print(Tax)
print(TaxList)

TaxList.append(30)
NewTax = tuple(TaxList)

print(TaxList)
print(NewTax)

(tax1, tax2, tax3, tax4) = Tax
print(tax1, tax2, tax3, tax4)

a=1
b=10
print("a= ", a, "\tb = ", b)

temp = a
a=b
b=temp
print("a= ", a, "\tb = ", b)

(a,b) = (b,a)
print("a= ", a, "\tb = ", b)

marketing = ['loyality program', 'client promotion', 'market research']

marketing.append('public relations')

print(marketing[3])

marketing.insert(2, 'investor realtions')

emailMarketing = marketing.copy()
emailMarketing.sort()

internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)

newTuple = tuple(emailMarketing)
print(newTuple)
print(emailMarketing)
