class employee:
    a = 1

class programmer(employee):
    b = 2

class manager(programmer):
    c = 3
    
    
a = employee()
print(a.a)
# print(a.b)  gives error 

b = programmer()
print(b.a)
print(b.b)
# print(b.c)  gives error

c = manager()
print(c.a)
print(c.b)
print(c.c)
