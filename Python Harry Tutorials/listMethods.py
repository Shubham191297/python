l = [22,56, 1,2,4,6]

# print(l)

# l.append(7)
# print(l)

# l.sort()
# print(l)

# l.sort(reverse=True)
# print(l)

# l.reverse()
# print(l)

# To get index of element in the list - gives for first occurence
print(l.index(1))

# Same reference is created for different objects
m = l
# m[0]= 0
# print(m)
print(l)

# To create a copy of object so that its not mutable
n = l.copy()
n[0]=0
print(n)

# To insert at a specific index
l.insert(1,899)
print(l)

# To extend a list using other list
a = [0,9,13,99]
l.extend(a)
print(l)

# If you want to create new list by appending and instead not mutating the original list 
b = a + [6,8]
print(b)