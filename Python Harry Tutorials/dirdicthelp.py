x = [1,2,3]

# dir method is useful tool for discovering what you can do with an object. The dir function returns a list of all the attributes and methods available for an object.

print(dir(x))

# __dict__ returns a dictionary representation of an objects attributes.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        self.version = 1
        
p = Person("Shubham",26)
print(p.__dict__)

# help function is used to get help documentation for an object, including a description of its attributes and methods.

