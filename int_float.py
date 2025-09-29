import sys
print(sys.maxsize)

five = 5
three = 3
print(five//three)

print(five % three)

print(float('inf')>999999999999999999999999999999999999999999)

name = 'Maciek'
age = 26
daysInYear = 365
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,age*daysInYear))

message = '%s is %d years old, so is about %d days old'
print(message % (name,age,age*daysInYear))

#Chris is 17 years old, so is about 6205 days old
name = 'Chris'
age = 17
print(message % (name,age,age*daysInYear))

#1234567890 divided by 12345 is  100005 and the rest is 6165
a = 1234567890
b = 12345
message2 = '%d divided by %d is %d and the rest is %d' 
print(message2 % (a, b, a//b, a%b))

message2 = '{0:d} divided by {1:d} is {2:d} and the rest is {3:d}' 
print(message2.format(a, b, a//b, a%b))
