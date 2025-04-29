# This is the example of hybrid inheritance

class BaseClass:
    pass

class DerivedClass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass

class DerivedClass3(DerivedClass1, DerivedClass2):
    pass

# Hierarchical inheritance is a type of inheritance in OOP where multiple subclasses inherit from a single base class

class Base:
    pass

class D1(Base):
    pass

class D2(Base):
    pass

class D3(D1):
    pass