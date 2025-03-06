class Employee:
    a = 1
    @classmethod # it will show class attribute over instance value
    def show(cls):
        print(f"th value of a is {cls.a}")

e = Employee()
e.a = 45
e.show()

# note that here if we change the value of a using the class instance then the instance value will prevail rather than class value but to make the class value prevail over the object value then we need to use the class method @ classmethod


# self means the object on which the method is running
# cls means its the class itself on which the method is running 