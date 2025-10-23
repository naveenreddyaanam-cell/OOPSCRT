class Employee:
    def __init__(self, name, salary):
        self.name = name          
        self.__salary = salary
        
    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Naveen", 50000)
print(emp.name)       
emp.show_salary()
        
