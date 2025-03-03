n = 3
m = n
j = 1

for i in  range(1,n+1):
    print(" " * m + "*" * j,end="")
    j += 2
    m -= 1
    print()
    