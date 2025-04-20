def cube(x):
    return x*x*x

# print(cube(2))



# Map is used for transformation of values to new values
l = [1,2,4,6,8,10]

newl = list(map(cube,l))
print(newl)

# Filter is used to filter out the elements we want as per condition
def filter_function(a):
    return a>4

newnewl = list(filter(filter_function,l))
print(newnewl)

# Reduce is used to boil out the values to single value

from functools import reduce
sum = reduce(lambda x,y: x+y,l)
print(sum)