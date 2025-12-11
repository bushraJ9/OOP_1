#Task 01
'''
OOP Project: Employee & Manager System
This project demonstrates the four pillars of Object-Oriented Programming (OOP):
- Abstraction: Person class defines a generic interface via show_info().
-Encapsulation: Employee and Manager attributes are contained within their classes.
-Inheritance: Manager inherits from Employee, Employee inherits from Person.
-Polymorphism: show_info() is overridden to display appropriate info for each class.

Creates multiple Employee objects and a Manager object, and prints their information.
'''


class Person:
    def show_info(self):
        pass


class Employee(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


    def show_info(self):
        return f"Employee: {self.name}, Age: {self.age}, Dept: {self.department}"


class Manager(Employee):
    def __init__(self, name, age, department, team_size):
        super().__init__(name, age, department)
        self.team_size = team_size

    def show_info(self):
        return f"Manager: {self.name}, Age: {self.age}, Department: {self.department}, Team Size: {self.team_size}"


Employee1 = Employee("Rahaf", 24, "SOC L1")
Employee2 = Employee("Taif", 23, "SOC L1")
Employee3 = Employee("Reem", 26, "SOC L2")
Employee4 = Employee("Abdullah", 28, "SOC L2")
Employee5 = Employee("khalid", 30, "SOC L3")
Manager1 = Manager("Bushra", 24, "SOC Leader", 5)

print(Employee1.show_info())
print(Employee2.show_info())
print(Employee3.show_info())
print(Employee4.show_info())
print(Employee5.show_info())
print(Manager1.show_info())


