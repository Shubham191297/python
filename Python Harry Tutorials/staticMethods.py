class Math:
    def __init__(self,num):
        self.num = num
        
    def add_to_num(self,n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b):
        return a + b
    
    
a = Math(5)
print(a.num)
a.add_to_num(6)
print(a.num)

# Static methods belong to class rather than to instance of class. Can only be called from constructor function of class
print(Math.add(3,6))