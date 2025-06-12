# 26 - Advanced Functions

# --- Functions Returning Functions ---
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

multiply_by_3 = make_multiplier(3)
print(multiply_by_3(10))  # 30

# --- Functions as Arguments ---
def apply_operation(x, y, operation):
    return operation(x, y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(apply_operation(5, 3, add))       # 8
print(apply_operation(5, 3, subtract))  # 2

# --- Closures (Remembering State) ---
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2

# --- Decorator (Manual Application) ---
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def greet():
    return "hello"

greet_upper = uppercase_decorator(greet)
print(greet_upper())  # HELLO

# --- Decorator (Using @ Syntax) ---
@uppercase_decorator
def welcome():
    return "welcome"

print(welcome())  # WELCOME
