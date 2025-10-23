Inheritance in python

The process of inheriting the properties of the parent class into a child class is called inheritance.
the existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.

TYPES OF INHERITANCE

In python, based upon the number of child and parent classes involed, there are five types of inheritance.the types of inheritance are listed below.

1.SINGLE INHERITANCE :- In single inheriitance,a child class inherits from a single-parent class.here is one child class and one parent class.
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def show_role(self):
        print(self.name, "is an employee")

emp = Employee("Sarah")
print("Name:", emp.name)
emp.show_role()


2.MULTPLE INHERITANCE :- In multiple inheritance, a child class can inherit from more than one parent class.

class Person:
    def __init__(self, name):
        self.name = name

class Job:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Job):  # Inherits from both Person and Job
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print(self.name, "earns", self.salary)

emp = Employee("Naveen", 50000)
emp.details()

3.MULTILEVEL INHERITANCE :- In multilevel inheritance, a class is derived from another derived class (like a chain).

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def show_role(self):
        print(self.name, "is an employee")

class Manager(Employee):  # Manager inherits from Employee
    def department(self, dept):
        print(self.name, "manages", dept, "department")

mgr = Manager("Nani")
mgr.show_role()
mgr.department("HR")

4.HIERARECHIAL INHERITANCE :- In hierarchical inheritance, multiple child classes inherit from the same parent class.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "works as an employee")

class Intern(Person):  
    def role(self):
        print(self.name, "is an intern")

emp = Employee("Sai")
emp.role()

intern = Intern("Sudheer")
intern.role()


5.HYBRID INHERITANCE :- Hybrid inheritance is a combination of more than one type of inheritance.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "is an employee")

class Project:
    def __init__(self, project_name):
        self.project_name = project_name

class TeamLead(Employee, Project):  # Hybrid Inheritance
    def __init__(self, name, project_name):
        Employee.__init__(self, name)
        Project.__init__(self, project_name)

    def details(self):
        print(self.name, "leads project:", self.project_name)

lead = TeamLead("Ram", "AI Development")
lead.role()
lead.details()
