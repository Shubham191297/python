class Employee:
    # This is generic class variable which we dont want to modify for the instances and keep it same for a class
    # First the code checks for instance variable with same name if it exists then takes over else class variables take priority
    companyName = "Meta"
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.05
    
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")
        
emp1 = Employee("Shubham")
# Instance variables can be modified by accessing directly as they are directly associated with instance
emp1.raise_amount = 0.3
emp1.companyName = "Apple"
emp1.showDetails()

emp2 = Employee("Abhishek")
emp2.showDetails()

# Company name can also be changed using below
Employee.companyName = "Google"