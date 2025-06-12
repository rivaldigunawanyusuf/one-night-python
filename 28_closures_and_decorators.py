# 28 - Closures and Decorators

# --- Closure: Function returning another function and "remembers" variables ---

def multiplier(factor):
    def multiply(x):
        return x * factor  # factor is remembered even after outer function ends
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(4))  # 12


# --- Basic Decorator ---

def greet_decorator(func):
    def wrapper():
        print("Before the function runs")  # pre-processing
        func()
        print("After the function runs")   # post-processing
    return wrapper

@greet_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function runs
# Hello!
# After the function runs


# --- Decorator with Arguments ---

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi, {name}!")

greet("Alice")
# Output:
# Hi, Alice!
# Hi, Alice!
# Hi, Alice!
