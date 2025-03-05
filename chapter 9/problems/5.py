with open("log.txt") as l:
    if("python" in l.read()):
        print("python word found in log.txt")
    else:
        print("not found")