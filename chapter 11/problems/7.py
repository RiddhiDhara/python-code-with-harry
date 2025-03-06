class Vector:
    def __init__(self, l): 
        self.l = l

    
    
    def __len__(self):
        return len(self.l)

# Test the implementation
v1 = Vector([1, 2, 3]) 
print(len(v1))

#  __len__ is a special (dunder) method that allows the len() function to work on instances of Vector.