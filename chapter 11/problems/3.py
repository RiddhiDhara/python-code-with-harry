# class employee:
#     def setSalary(self,salary):
#         self.salary = salary
#         print(f"your salary is set to {self.salary}")
#     def incrementSalary(self,increment):
#         self.salary += increment
#         print(f"Your salary incremented by {increment}")
#     def showSalary(self):
#         print(f"your salary is {self.salary}")

# e = employee()
# e.setSalary(234)
# e.incrementSalary(20)
# e.showSalary()


class Employee:
    increment = 20
    salary = 234

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.increment)
