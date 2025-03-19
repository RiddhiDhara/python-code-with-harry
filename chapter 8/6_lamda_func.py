# here we will be talking about lambda function in python

# A lambda function in Python is an anonymous (unnamed) function that can have any number of arguments but only one expression.

# SYNTAX : 
# lambda arguments: expression

# the above syntax is equivaluent to :

# def func(arguments):
#     return expression


# this is a normal syntax of a function in python
def func(x,y):
    return x + y
print("using normal function : ",func(3,4))


# the above function can be written using lambda

func1 = lambda x,y : x + y
print("using lambda function : ",func1(3,4))
