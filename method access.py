#Access private member outside of a class using an instance method
class Employee:

    def __init__(self, name, salary):

        self.name = name

        self.__salary = salary

    def show(self):

        print("Name: ", self.name, 'salary:', self.__salary)

emp = Employee('Nani', 10000)

emp.show()
