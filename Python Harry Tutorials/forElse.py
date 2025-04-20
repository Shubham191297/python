for i in range(5):
    print(i)
    if(i==3):
        break
# As we are breaking the loop else block will not execute
else:
    print("Sorry no i to print")
    
j = 0
while(j<7):
    print(j)
    j = j + 1
    if(j==3):
        break
else:
    print("Sorry no i for printing")