class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"{self.i} i + {self.j} j + {self.k} k"
    
    # If here add method was already present before and we define it here then it will be overloaded with new add method but here add method is an operator
    def __add__(self,x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    
v1 = Vector(3,5,6)
print(v1)
v2 = Vector(4,7,-1)
print(v1)
print(v1 + v2)
print(type(v1 + v2))