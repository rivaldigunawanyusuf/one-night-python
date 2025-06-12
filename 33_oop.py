# 33 - OOP Summary: Class, Inheritance, Encapsulation, Polymorphism

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def work(self):
        return f"{self.name} is working..."

    @property
    def salary(self):
        return self._salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def work(self):
        return f"{self.name} is managing {self.department}"


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        return f"{self.name} is coding in {self.language}"


# --- Demo Polymorphism ---
staff = [
    Manager("Alice", 9000, "Sales"),
    Developer("Bob", 7000, "Python"),
    Employee("Charlie", 5000)
]

for person in staff:
    print(person.work())  # Calls respective overridden method
    print("Salary:", person.salary)

# Alice is managing Sales
# Salary: 9000
# Bob is coding in Python
# Salary: 7000
# Charlie is working...
# Salary: 5000
