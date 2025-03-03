l1 = ["Reed", "Soham", "Sachin", "Rahul"]
found = False

for i in l1:
    if i.startswith("S"):
        print(i)
        found = True
if not found:
    print("no name found with S ")