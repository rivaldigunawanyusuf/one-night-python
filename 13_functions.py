# 13 - Functions

# Defining a simple function
def greet():
    print("Hello!")

greet()  # call the function

# Function with parameters
def greet_person(name):
    print("Hello,", name)

greet_person("Alice")
greet_person("Bob")

# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print("Result:", result)

# Function with default parameter
def greet_with_default(name="Guest"):
    print("Hi,", name)

greet_with_default()  # uses default
greet_with_default("Eve")  # overrides default

# -----------------------------------
# Using *args - Multiple Positional Arguments

def print_shopping_list(*items):
    print("Shopping List:")
    for item in items:
        print("-", item)

print_shopping_list("Milk", "Eggs", "Bread")
print_shopping_list("Apple", "Banana")

# *args packs all extra positional arguments into a tuple

# -----------------------------------
# Using **kwargs - Multiple Keyword Arguments

def create_profile(**details):
    print("User Profile:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

create_profile(name="John", age=28, country="USA")
create_profile(username="alice123", verified=True)

# **kwargs packs all extra keyword arguments into a dictionary

# -----------------------------------
# You can combine them (order matters)
def mixed_example(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

mixed_example(1, 2, 3, 4, x=5, y=6)

# Output:
# a: 1
# b: 2
# args: (3, 4)
# kwargs: {'x': 5, 'y': 6}
