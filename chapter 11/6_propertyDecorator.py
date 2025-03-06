class Employee:
    a = 1
    @classmethod # it will show class attribute over instance value
    def show(cls):
        print(f"the value of a is {cls.a}")
        
    @property # @property makes name() behave like an attribute, even though it’s a method.
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter # @name.setter allows modification of name using assignment syntax (e.name = "Riddhi Dhara").
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45 
e.name = "Riddhi Dhara"
print(e.fname, e.lname )
e.show()


# abstraction means that the behind working is hidden from the user
# encapsulation means that multiple working components are excapsulated/contained in a class