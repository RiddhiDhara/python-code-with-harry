class Employee:  # base class
    company = "ITC"
    def show(self):
        print(f"the name of the employee is {self.name} anf the salary is {self.salary}")
        
        
class Programmer(Employee): # child / derived class
    def showLanguage(self):
        print(f"the name is {self.name} and he is good at {self.language} language.")
        
        
        
a = Employee()
b = Programmer()
print(a.company, b.company)






# ========================================================================
        
# class Programmer:
#     company = "ITC InfoTech"
#     def show(self):
#         print(f"the name is {self.name} anf the salary is {self.salary}")
        
#     def showLanguage(self):
#         print(f"the name is {self.name} and he is good at {self.language} language.")


# note that suppose we need the attributes and properties of another class in some other class then rather than copying the content we can use the concept of inheritence 


# here the programmer class is inheriting the employee class with all its attributes and methods hence able to print the company name inherited from the employee class