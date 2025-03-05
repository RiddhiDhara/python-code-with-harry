with open("match1.txt") as f:
    content1 = f.read()
with open("match2.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("both files are same!!")
else:
    print("both are not same!!")
