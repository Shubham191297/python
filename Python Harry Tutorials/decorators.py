def greet(fx):
    # Way to pass function with arguments onto our decorator function so that they get accepted
    def mfx(*args,**kwargs):
        print("Good morning!")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world")
    
# @greet
def add(a,b):
    print(a+b)    
    
hello()

# Other way to run is greet(hello)()

greet(add)(1,4)


# Decorators - feature in python used to add functionality of functions and methods by modifying its behaviour without modifying its source code