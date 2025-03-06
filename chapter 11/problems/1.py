class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show2D(self):
        print(f"{self.i}i + {self.j}j")
    
class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j) #inheriting the i and j and from TwoDVector
        self.k = k
    def show3D(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")
        
a = TwoDVector(1,2)
a.show2D()
b = ThreeDVector(5,2,3)
b.show3D()