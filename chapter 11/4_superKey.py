class employee:
    def __init__(self):
        print("contructor of Employee")
    a = 1

class programmer(employee):
    def __init__(self):
        super().__init__()
        print("contructor of Programmer")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("contructor of Manager")
    c = 3
    
    
# a = employee()
# print(a.a)
# # print(a.b)  gives error 

# b = programmer()
# print(b.a)
# print(b.b)
# # print(b.c)  gives error

c = manager()
print(c.a)
print(c.b)
print(c.c)


# note that here when ever we are creating an object of any particular class then only that class constructor is run and others not 
# but if we want to run all other constructor of the inherited class from the inheriting class object then we use super keyword!!
# ✅ super() allows access to parent class methods and constructors.

