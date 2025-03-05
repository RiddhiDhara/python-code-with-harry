class hello:
    a = "hello"  # class attribute
    
    def getInfo(self):
        print(f"the value of a is {self.a}")
        
b = hello()
b.a = "Bhalo" # instance attribute

b.getInfo()
