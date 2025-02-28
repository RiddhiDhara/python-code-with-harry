fruits = ["apple", "pineapple", "Orange", "Mango", "Licci" ]

# adding at the back

fruits.append("banana")
print(fruits)

# add at given index

fruits.insert(1,"guava")
print(fruits)

# removing from the back but can also be removed from any given position

fruits.pop(-2)
print(fruits)

# removing first occurance from the list by mentioning the element present

fruits.remove("banana")
print(fruits)

# sorting a list

l1 = [55,89,12,47,36]

l1.sort()
print(l1)

l1.reverse()
print(l1)