num = 4

with open("table.txt","a") as f:
    for i in range(1,11):
        f.write("{} x {} = {}\n".format(num,i,num*i))
print("file is written")