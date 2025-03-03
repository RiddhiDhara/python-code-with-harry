# functions with default parametres

def param(a,b,c = 25):
    return a+b+c

res = param(5,65)
print(res)

red = param(5,65,10)
print(red)

# note that when arg valueof the default param is provided then the default val is replaced by the new value else default is presumed