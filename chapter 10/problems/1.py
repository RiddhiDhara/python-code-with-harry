class programmer:
    company = "Microsoft"
    
    def __init__(self,name,role,language):
        self.name = name
        self.role = role
        self.language = language
    
    @staticmethod
    def greet():
        print(f"Welcome to Microsoft")
        
    def getInfo(self):
        print(f"{self.name} is a {self.role} at {self.company} who works with {self.language}.")
        
        
programmer.greet()
riddhi = programmer("Riddhi","ML Engineer","Python")
riddhi.getInfo()
gourav = programmer("Gourav","SDE1","Java")
gourav.getInfo()
rohan = programmer("Rohan","Data Scientist","Rust")
rohan.getInfo()