class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    
e = Employee("Shubham",50000)

string = "Angu-20000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)