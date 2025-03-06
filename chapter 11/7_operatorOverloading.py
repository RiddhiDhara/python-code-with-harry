class number:
    def __init__(self,n):
        self.n = n
        
    def __add__(self,num): # this is for + operator
        return self.n + num.n

n = number(1)
m = number(2)

print(n+m)


# note that in oops everything is a class that means those operators are also classes and their default functionality can be changed using operator overloading 

# How This Works Internally
# n + m calls n.__add__(m).
# n.__add__(m) returns self.n + num.n, which is 1 + 2.
# The result 3 is printed.


# Operators in Python can be overloaded using the following methods: 
# p1+p2 # p1._add_(p2) 
# p1-p2 # p1._sub_(p2) 
# p1*p2 # p1._mul_(p2) 
# p1/p2 # p1._ truediv_ (p2) 
# p1//p2 # p1. _ floordiv_(p2) 

# Other dunder/magic methods in Python: 
# str__() # used to set what gets displayed upon calling str(obi)