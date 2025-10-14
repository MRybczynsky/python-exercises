# %%for candidate in range(2,31):
    for divider in range(2, candidate):
        if candidate % divider == 0:
            print("%2d is not a prime number - divider is %2d" % (candidate, divider))
            break
    else:
        print("%2d is prime" % candidate)

print('\n')

text = """Mechanical advantage is a measure of the force amplification achieved by using a tool,
mechanical device or machine system. The device trades off input forces against movement to obtain
a desired amplification in the output force. The model for this is the law of the lever. 
Machine components designed to manage forces and movement in this way are called mechanisms.
An ideal mechanism transmits power without adding to or subtracting from it. This means 
the ideal machine does not include a power source, is frictionless, and is constructed 
from rigid bodies that do not deflect or wear. The performance of a real system relative 
to this ideal is expressed in terms of efficiency factors that take into account departures from the ideal."""

words = text.split(' ')
short_text = ''
counter = 0

for word in words:
    short_text += word+' '
    counter += 1
    if counter>=20:
        print(short_text)
        break


# %%
