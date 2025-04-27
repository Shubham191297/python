# Access modifiers in python programming language are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance
'''
Public - Any variable or method in class in python is by default public and can be accessible via any instance of the class
Protected - Any variable or method in class which is meant to be accessed only by its class and subclass.
Private - Any variable which is restricted to be used only within inside the class but not by any object/subclass of that class 
'''

class Employee:
    def __init__(self,id):
        # self.name = "Shubham"
        # This indicates a private property. Still can be accessed.
        self.__name = "Shubham"
        self._id = id
        
class Coder(Employee):
    def info(self):
        print("I am a coder")
        
a = Employee(569)
# Cannot be accessed directly but can be accessed indirectly.
# print(a.__name)

# But can be accessed indirectly
# This is due to name mangling. It is technique used to protect class private and super class private attributes from being accidentally overwritten by subclasses.
print(a._Employee__name)

b = Coder(456)
# _id is accessible from sub class 
print(b.__dir__())