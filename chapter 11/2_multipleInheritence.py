class Employee:  # base class
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"the employee {self.name} works in {self.company}")
        
class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"out of all the langauge here is your language : {self.language}")
        
        
class Programmer(Employee,Coder): # child / derived class
    def showLanguage(self):
        print(f"the name is {self.name} and he is good at {self.language} language.")
        
        
        
a = Employee()
b = Coder()
c = Programmer()

c.showLanguage()
c.printLanguage()
c.show()


