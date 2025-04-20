# is compares the location of object in memory and = compares the exact value

a = 4
b="4"

print(a==b)
print(a is b)

# Now in below a and b both refer to same memory location where number 3 is stored. Python never waste memory in refering to a constant
a = 3
b = 3
print("\n")
print(a==b)
print(a is b)

# But if they are list/object as below then they are stored in different memory location
a = [1,2,4]
b = [1,2,4]

print("\n")
print(a is b)
print(a==b)