# def double(x):
#     return x*2

# In short used as a short hand function

double = lambda x:x*2
avg = lambda x,y:(x+y)/2

print(double(5))
print(avg(4,10))

# We can also use lambda function when we want to pass function into the function
def appl(fx, value):
    return 2 + fx(value)

print(appl(double,6))
