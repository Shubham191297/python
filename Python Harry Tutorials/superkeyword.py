# super keyword in python is used tto refer to parent class

class ParentClass:
    def parent_method(self):
        print("This is a parent method.")
        
class ChildClass(ParentClass):
    def parent_method(self):
        print("Shubham")
        super().parent_method()
    
    def child_method(self):
        print("This is a child method")
        super().parent_method()
        
cobj = ChildClass()
cobj.child_method()
cobj.parent_method()


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self,name,id,lang):
        # Instead of giving name and id 
        # self.name = name
        # self.id = id
        
        super().__init__(name, id)
        self.lang = lang
        
abhi = Employee("Abhishek","106")
shubham = Programmer("Shubham","569","Python")
print(abhi.name)