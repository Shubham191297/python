# Multiple inheritance is a powerful feature in OOP that allows a class to inherit attributes and methods from multiple parent classes.

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")
    
class Dancer:
    def __init__(self,dance):
        self.dance = dance 

    def show(self):
        print(f"The dance is {self.dance}")

# Which show will be called depends on the order in which we define classes inside ()
class DancerEmployee(Dancer,Employee):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name
        
o = DancerEmployee("Salsa","Emily")
print(o.name, o.dance)
o.show()

# To check which order is used to find and run any method inherited from multiple parent class we use mro
print(DancerEmployee.mro())