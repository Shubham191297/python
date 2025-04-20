import math
from math import sqrt, pi
from math import pow as p

num = math.floor(4.55555)
print(num)

print(math.sqrt(49))

print("Area of circle: ",math.pi*(7**2))

print(p(2,6))

# To print which variables and function are inside math library
print(dir(math))

print(math.nan,type(math.nan))

from newImportPack import shubham, welcome

welcome()
print(shubham)