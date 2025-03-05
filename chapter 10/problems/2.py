import math

class calculator:
    def __init__(self,num1):
        self.num1 = num1
    
    def findSquare(self):
        print(f"The square of the number {self.num1} is {self.num1**2}")
    def findCube(self):
        print(f"The cube of the number {self.num1} is {self.num1**3}")
    def findSquareRoot(self):
        print(f"The square root of the number {self.num1} is {math.sqrt(self.num1)}")


number = calculator(4)
number.findSquare()
number.findCube()
number.findSquareRoot()
        