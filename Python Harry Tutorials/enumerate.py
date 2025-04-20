marks = [12,56,32,98,12,45,1,4]

# index=0

# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Harry, awesome!")
#     index+=1

for index, mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("Harry, awesome!")
        
# If we replace index, mark with v, v will return a tuple

# To pass a different starting index into an argument we can do as below
fruits = ["kiwi","dragon fruit","avocado"]
for index, fruit in enumerate(fruits, start=1):
    print(index,fruit)