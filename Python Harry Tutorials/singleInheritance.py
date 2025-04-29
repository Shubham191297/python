# Single inheritance is a type of inheritance where a class inherits properties and behaviors from single parent class

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by an animal")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark")
        
class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Cat")
        self.breed = breed
        
    def make_sound(self):
        print("Meow")        
        
    def purr(self):
        print("I like to purr a lot")
        
    def jump_land(self):
        print(f"I can jump from any height and still land safe as I am {self.breed} cat")
        
d = Dog("Ruby","Labrador")
d.make_sound()

a = Animal("Ruby","Dog")
a.make_sound()

c = Cat("Elena","Kitty")
c.jump_land()
c.purr()