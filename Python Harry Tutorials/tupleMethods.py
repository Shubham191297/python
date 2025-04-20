countries=("India","China","Sri Lanka","Bangladesh")

countries2=("England","Italy","Germany","Spain","India")

totalCountries= countries+countries2
print(totalCountries)

# To count number of occurences of string
print(totalCountries.count("India"))

# To get the index of first occurence of an element in tuple
print(totalCountries.index("India"))

# To check the same in a specific range
print(totalCountries.index("India",5,10))