class hello:
    a = "hello"  # class attribute
    
    def getInfo(riddhi):
        print(f"the value of a is {riddhi.a}")
        
b = hello()
b.a = "Bhalo" # instance attribute

b.getInfo()