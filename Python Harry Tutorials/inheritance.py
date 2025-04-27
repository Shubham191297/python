class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")
        
        
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")
        
e1 = Employee("Abhishek",569)
e1.showDetails()
# e1.showLanguage()

e2 = Programmer("Nilay",796)
e2.showDetails()
e2.showLanguage()