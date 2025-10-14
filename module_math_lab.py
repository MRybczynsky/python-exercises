# %%import math

math.pi
# %%from math import *
# %%pi
# %%floor(pi)
# %%degree = 360
print(degree, " -> radian: ", degree*pi/180)

degree = 45
print(degree, " -> radian: ", degree*pi/180)

print(degree, " -> radian: ", radians(degree))

print("-------------------------------------")

small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38
small_pizza_price = 11.5
big_pizza_price = 15.6
family_pizza_price = 22

print("Small pizza: ", round(pi*pow(small_pizza_r,2),2))
print("Big pizza: ", round(pi*pow(big_pizza_r,2),2))
print("Family pizza: ", round(pi*pow(family_pizza_r,2),2))
print("\n")
print("Small pizza - price for m2: ", round((pi*pow(small_pizza_r,2)/small_pizza_price),2))
print("Big pizza - price for m2:", round((pi*pow(big_pizza_r,2)/big_pizza_price),2))
print("Family pizza - price for m2", round((pi*pow(family_pizza_r,2)/family_pizza_price),2))
print("\n")

math_ls = dir(math)
print(math_ls)

# %%
