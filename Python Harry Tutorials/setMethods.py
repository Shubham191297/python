s1 = {2,4,6,8}
s2 = {7,5,2}

# To concatenate two sets use union
print(s1.union(s2))

# To get intersection of two sets
print(s1.intersection(s2))

# below updates the stack with other elements
s1.update(s2)
print(s1,s2)

# What is difference between union and update. update changes the set values to include the values of the set specified insideself.
# While union needs to be passed on to new set
got1={"winterfell","kings landing","eyrie","twins","wall"}
got2={"riverrun","dorne","highgarden","eyrie"}

# Updates the got1 with intersection values
# got1.intersection_update(got2)
print(got1)


# To calculate symmetric difference. To find uncommon values from both the sets
# A U B - A n B = A ^ B
gotDiff = got1.symmetric_difference(got2)
print(gotDiff)

# To find simple difference use below
print(got1.difference(got2))

# To calculate difference of sets and update
# got1.difference_update(got2)
# print(got1)


# To check if given sets are disjoint sets
print(got1.isdisjoint(got2))

# To check if given set is subset or superset of a set
city1 = {"Diu","Udaipur","Abu","Indore"}
city2 = {"Diu","Abu"}
city3 = {"Jodhpur","Jaipur"}
print(city1.issubset(city2))
print(city1.issuperset(city2))
print(city2.issubset(city1))
print(city3.issubset(city1))

# to add single value to the set
city1.add("Surat")
print(city1)

# To add multiple items to a set use update

# To remove values from the set use remove / discard. Difference is if value is not present in set remove raises error while discard  does'nt
city1.remove("Abu")
print(city1)

# To remove an item from the top we use pop it means last element but the element is not fixed as sets are unordered
# But we can instead access the popped value
cityPopped = city1.pop()
print(cityPopped)

# del this is a keyword and not a method which deletes the entire set in one command
# del city1
# print(city1)

# To clear all the values from the set
city3.clear()
print(city3)

if "Abu" in city1:
    print("City is present!")