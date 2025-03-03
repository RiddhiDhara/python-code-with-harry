# function calling itself inside until the base criteria is met is called a recursion 

def req(n):
    if(n == 1 or n==0):
        return 1
    return n * req(n-1)


res = req(5)

print(res)