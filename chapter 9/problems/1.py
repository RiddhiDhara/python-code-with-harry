found = False

with open("poem.txt") as f:
    line = f.readline()
    while(line != ""):
        if "twinkle" in line:
            found = True
        line = f.readline()
    if found:
        print("word twinkle found!!")
    else:
        print("word twinkle not found!!")
        
        