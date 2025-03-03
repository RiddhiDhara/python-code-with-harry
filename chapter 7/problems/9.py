import math

n = 3
j = int(math.floor(n/3))

for i in  range(0,n):
    if(i == j):
        print("*" * ((n-1)//2),end="")
        print(" ",end="")
        print("*" * ((n-1)//2),end="")
    else:
            print("*" * n,end="")
    print()
    