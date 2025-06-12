# 34 - Python Summary File

# --- Variables and Data Types ---
name = "Alice"
age = 25
is_active = True
scores = [90, 85, 92]
user = {"name": "Alice", "age": 25}

# --- String Methods and f-strings ---
message = f"{name.upper()} is {age} years old."  # 'ALICE is 25 years old'

# --- Input ---
# user_input = input("Enter your name: ")  # Uncomment for interactive use

# --- Arithmetic and Comparison Operators ---
total = age + 5  # 30
print(total > 20)  # True

# --- Conditional Statements ---
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# --- Logical and Chained Conditions ---
if age > 18 and is_active:
    print("Eligible")

# --- Loops and Range ---
for i in range(3):
    print(i)

count = 0
while count < 3:
    print(count)
    count += 1

# --- Functions and Arguments ---
def greet(name="User"):
    return f"Hello, {name}!"

print(greet("Bob"))

def add_all(*args):
    return sum(args)

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# --- Built-in Functions ---
print(len(scores))  # 3
print(sorted(scores))  # [85, 90, 92]

# --- List Manipulations ---
scores.append(88)
scores[0] = 95
print(scores[1:4])  # slicing

# --- Dicts and Sets ---
data = {"a": 1, "b": 2}
unique = {1, 2, 2, 3}

# --- Comprehensions ---
squares = [x * x for x in range(5)]
even_dict = {x: x % 2 == 0 for x in range(5)}

# --- Boolean Context ---
if []:  # empty list is falsy
    print("Not empty")
else:
    print("Empty")

# --- Scope and Global ---
counter = 0
def increment():
    global counter
    counter += 1

# --- Exception Handling ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# --- Lambda Functions ---
double = lambda x: x * 2
print(double(4))  # 8

# --- Closures and Decorators ---
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times3 = make_multiplier(3)
print(times3(10))  # 30

# --- OOP ---
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

dog = Dog("Buddy")
print(dog.speak())  # Buddy barks
