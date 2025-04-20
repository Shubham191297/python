x = 4
print(x)

def hello():
    x = 5
    y = 9
    print(f"Local variable x is {x}")
    print("Hello Shubham")
    
    # To change value of X use below
    # global x
    # x = new Value
    

hello()
print(f"Global variable x is {x}")