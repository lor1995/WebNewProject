class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} received a raise of Php{amount}. New salary: Php{self.salary}")
    
    def display_employee(self):
        print(f"Employee Details: {self.name}, Position: {self.position}, Salary: Php{self.salary}")

# Creating an employee and performing actions
employee = Employee("John Smith", "Software Engineer", 70000)
employee.display_employee()
employee.give_raise(5000)
employee.display_employee()