ep1={122: 39,123:89,160: 70, 560: 90}
ep2={222: 67,566: 55}

print(ep1)

# To update the dictionary
ep1.update(ep2)
print(ep1)

# to clear all the elements from dictionary
# ep1.clear()
# print(ep1)

# To create an empty dictionary
ep3={}

# To remove a key value pair from dictionary
ep1.pop(160)
print(ep1)

# To remove last item from the dictionary
ep1.popitem()
print(ep1)


# To delete the entire dictionary use del keyword
# del ep1
# print(ep1)

# To delete specific element from an array
# del ep1[560]