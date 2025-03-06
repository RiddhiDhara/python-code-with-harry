class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def __add__(self,c2):
        return complex(self.r + c2.r,self.i + c2.i)
    
    def __mul__(self,c2):
        realPart = self.r * c2.r - self.i * c2.i
        imgPart = self.r * c2.r + self.i * c2.i
        return complex(realPart,imgPart)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = complex(5,9)
c2 = complex(3,7)

print(c1 + c2)
print(c1 * c2)