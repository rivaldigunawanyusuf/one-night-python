# 29 - Classes and Objects

# --- Defining a Class ---
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name  # instance variable
        self.age = age    # instance variable

    def greet(self):  # instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# --- Creating Objects (Instances) ---
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

p1.greet()  # Hello, my name is Alice and I am 30 years old.
p2.greet()  # Hello, my name is Bob and I am 25 years old.

# Accessing and modifying attributes
print(p1.name)  # Alice
p1.age = 31
print(p1.age)   # 31
