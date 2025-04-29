# Multilevel inheritance is type of inheritance in OOP where a derived class inherits from another derived class.
# This type of inheritance allows you to build a hierarchy of classes where one class builds upon another class, leading to more specialized class.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def show(self):
        print(f"I am an animal named {self.name} of species - {self.species} and I live in woods")
        
class Reptile(Animal):
    def __init__(self, name, category, group ):
        Animal.__init__(self, name, species="Crocodylia")
        self.group = group
        self.category = category
        
    def show(self):
        Animal.show(self)
        print(f"I am {self.category} of category {self.group} and we crawl on land and lay eggs for reproduction")
        
class Crocodile(Reptile):
    def __init__(self, name, category):
        Reptile.__init__(self, name, category, group="reptiles")
    
    def show(self):
        Reptile.show(self)
        print(f"I am a crocodile and I can live in both Land and water. My nick name is {self.name}")
        
        
c = Crocodile("Salar","Crocodile")
c.show()

r = Reptile("Salar","crocodile","reptiles")
# r.show()

a = Animal("Salar","Crocodylia Pylia")
# a.show()
print(Crocodile.mro())