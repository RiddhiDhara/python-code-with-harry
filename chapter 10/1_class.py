class Employee:
    language = "python" # class attribute
    salary = 1200000 # class attribute
    
riddhi = Employee()
riddhi.name = "Riddhi" # object/instance attribute
print(riddhi.name,riddhi.language,riddhi.salary)

harry = Employee()
harry.name = "Harry" # object/instance attribute
print(harry.name,harry.language,harry.salary)


# note that here name is object/instance attribuet and language and salary are class attribute as they directly belong to the class

# note that instance attribute takes preference over class attribute during assignment and retrival 