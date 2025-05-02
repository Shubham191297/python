# It is a way to store the mechanism for generating the values on the fly. Values are not stored

def my_generator():
    for i in range(5):
        yield i
    
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))