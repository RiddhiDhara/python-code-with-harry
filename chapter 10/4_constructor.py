class Employee:
    company = "Google"
    
    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        
    def greet(self):
        print(f"Hello there Welcome to {self.company}")
    
    def getInfo(self):
        print(f"I am a SD1 at {self.company}. I am {self.name} with salary {self.salary} and I use {self.language}")


riddhi = Employee("Riddhi","Python",1200000)
riddhi.greet()
riddhi.getInfo()