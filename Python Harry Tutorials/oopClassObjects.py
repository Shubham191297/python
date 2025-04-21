class Person:
    name="Shubham"
    occupation="Site Reliability Engineer"
    networth = 10
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
a.name = "Angu"
a.occupation = "Teacher"

print(a.name,a.occupation)
a.info()

b = Person()
b.name = "Stuti"
b.occupation = "Data Associate"
b.info()