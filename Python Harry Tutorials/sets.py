# Set are unordered unchangeable collection of unique elements
nums = {1,2,4,5,7,2,1}

print(nums)

info={"Angu","Shubham",True,"Shubham",7, False}
print(info)

# The below does not create empty set instead creates empty dictionary as syntax of both contains { starting so it is considered empty dict
shubham={}
print(type(shubham))

# To define an empty set
angu = set()
print(type(angu))

# To define an empty tuple
manish = ()
print(type(manish))

for value in info:
    print(value)