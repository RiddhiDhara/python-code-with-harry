class Employee:
    language = "python" # class attribute
    salary = 1200000 # class attribute
    
riddhi = Employee()
riddhi.language = "Javascript"
print(riddhi.language,riddhi.salary)


# note that here name is object/instance attribuet and language and salary are class attribute as they directly belong to the class

# note that instance attribute takes preference over class attribute during assignment and retrival 