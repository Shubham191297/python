marks = [3,5,6,"20",True]

# print(marks)
# print(type(marks))

# print(marks[0])
print(marks[-2])

if 20 in marks:
    print("Yes")
else:
    print("No")
    
if "sh" in "shubham":
    print("yes")
else:
    print("no")
    
# to print the list
print(marks)
print(marks[:])
print(marks[1:])
print(marks[1:-1])

# jump index
print(marks[1:-1:2])

# List comprehension
lst=[i for i in range(5)]
print(lst)
lst=[i for i in range(5) if i%2==0]
print(lst)