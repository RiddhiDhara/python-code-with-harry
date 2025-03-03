num = 11
found = False

for i in range(2,(num//2)+1):
    if(num % i == 0):
        found = True
        print(f"{num} not prime")
        break
if not found:
    print(f"{num} is prime")
    