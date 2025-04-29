class Employee:
    def __init__(self,name):
        self.name = name
    
    # This is a special method created with __ but used directly as magic method
    def __len__(self):
        return len(self.name)
    
    # This will print the representation of object
    def __str__(self):
        return f"The name of the employee is {self.name} str"

    # This is used as a fall back method
    def __repr__(self):
        return f"The name of the employee is {self.name} repr"
    
    def __call__(self):
        print("Hey I am better")
# print(len(e))