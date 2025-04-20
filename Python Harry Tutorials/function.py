a=9
b=8

gmean=(a*b)/(a+b)

print(gmean)

def calculateGmean(a,b):
    gmean=(a*b)/(a+b)
    print(gmean)
    
def isGreater(a,b):
    if(a>b):
        print(a,"is greater than",b)
    elif(b<a):
        print(b,"is greater than",a)
    else:
        print("Both are equal")
    
calculateGmean(5,8)
isGreater(4,4)

# To just declare a function and define 
def isLesser(a,b):
    pass