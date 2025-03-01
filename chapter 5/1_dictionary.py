# dictionary is a data structure that helps to store values in a the form of key value pairs

dict = {
    "name" : "Riddhi",
    "age" : 25,
    "girl" : False
}

# accessing the value using the key

print(dict["name"])

# printing the keys and the values

print(dict.items())

# inserting in the dict

dict["gf"] = "No"

print(dict)

# printing only the values of the dict

print(dict.values())

# updating the dict since the dict is mutable

dict.update({"age" : 21})

print(dict)

# getting a existing key in the dict

print(dict.get("hello"))