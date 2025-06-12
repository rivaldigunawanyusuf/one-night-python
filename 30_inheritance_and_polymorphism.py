# 30 - Inheritance and Polymorphism

# --- Base Class ---
class Animal:
    def __init__(self, name):
        self.name = name  # common attribute

    def speak(self):
        return "Some sound"  # base implementation


# --- Derived Classes ---
class Dog(Animal):
    def speak(self):
        return "Woof"  # overridden method


class Cat(Animal):
    def speak(self):
        return "Meow"  # overridden method


# --- Polymorphism in Action ---
animals = [Dog("Buddy"), Cat("Whiskers"), Animal("Creature")]

for animal in animals:
    print(f"{animal.name} says {animal.speak()}")  # Polymorphic behavior

# Buddy says Woof
# Whiskers says Meow
# Creature says Some sound
