names="Shubham,Shradha"

# To extract part of a string
print(names[0:7])

# To get length of a string
print(len(names))

# extract characters from a string
print(names[0:4])
print(names[1:4])
# Similar
print(names[:4])

# To extract all elements of a string. Python by default puts 0 in beginning and length of string in ending
print(names[:])

# To extract elements from starting till before ending use below
print(names[0:-5])

print(names[0:len(names)-3])

print(names[-1:len(names)-3])
print(names[-4:-1])

for str in "Shradha":
    print(str)