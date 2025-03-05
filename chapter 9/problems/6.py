

with open("log.txt") as l:
    lines = l.readlines()
    
lineno = 1
for line in lines:
    if("python" in line):
        print(f"python word found in log.txt at line {lineno}")
        break
    lineno += 1
else:
    print("python not present")