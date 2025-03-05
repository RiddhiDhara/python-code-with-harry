with open("donkey.txt", "r") as f:
    lines = f.readlines()

with open("donkey.txt", "w") as f:
    for line in lines:
        f.write(line.replace(line, "######\n"))  # Replace each line individually

print("File is written!!")
