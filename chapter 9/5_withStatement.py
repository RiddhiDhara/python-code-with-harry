# we will perfomr thw same operation as the previous ways but using with statement we dont have to close the opened files explicitely

with open("file.txt") as f:
    print(f.read())
    
    
    