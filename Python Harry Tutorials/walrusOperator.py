# Allows you to assign a value to variable within an expression.
numbers = [1,2,3,4,5]
a = True

print(a:=False)

while (n:= len(numbers)) > 0:
    print(numbers.pop())
  
# Below example is without using the walrus operator the simple way.  
    
# foods = list()
# while True:
#     food = input("What food do you like?:")
    
#     if food == "quit":
#         break
#     foods.append(food)

# Using the walrus operator
foods = list()
while(food:=input("What food do you like?:")!="quit"):
    foods.append(food)