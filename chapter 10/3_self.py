class Employee:
    language = "python" # class attribute
    salary = 1200000 # class attribute
    
    @staticmethod # making the method as static
    def greet():
        print("hello there good morning!!")
    
    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
        
riddhi = Employee()
riddhi.greet()
riddhi.getInfo()

# here actually 1 argument gets automatically passes which is Employee.getInfo(riddhi) but in the getInfo function there is no param to handle the arg there we use self


# note that in the function greet() we donot need self since we dont need to pass the object so to restrict the function from using object we can mark the function as a static function 