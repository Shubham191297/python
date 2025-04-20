def average(a=1,b=9):
    print("The average is ",(a+b)/2)
    
average(4,5)
average()
average(5)
average(b=1)

# Keyword arguments
average(b=19,a=11)

# required arguments. In below a is required
# def average(a,b=9):
#     print("The average is ",(a+b)/2)
def averageList(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    # print("Average is:",sum/len(numbers))
    return sum/len(numbers)
    
avg = averageList(3,4,6,9,2)
print(avg)

# of type dictionary
def nameGreet(**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])
    
nameGreet(fname="Shradha",mname="Digamber",lname="Baloni")