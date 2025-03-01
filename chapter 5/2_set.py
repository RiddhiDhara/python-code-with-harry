# getting started with sets

set1 = {1,56,89,41,52}
set2 = {2,56,48,41,52}

print(set1)
print(set2)

# performing set operation 

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.issubset(set1))

# creating an empty set 

set3 = set() # dont use set3 = {} since it creates a empty dict

# other basic methods

set3.add(4)
set3.add(25)

set3.remove(4)
