# 22 - Variable Scope (local, global, nonlocal)

# --- Local Scope ---
def greet():
    message = "Hello"
    print(message)  # Hello

greet()
# print(message)  # NameError: message is not defined


# --- Global Scope ---
language = "Python"

def show_language():
    print(language)  # Python

show_language()

count = 10

def increment_wrong():
    count = count + 1  # UnboundLocalError
    print(count)

# increment_wrong()  # Uncomment to trigger the error

def increment_right():
    global count
    count = count + 1
    print(count)  # 11

increment_right()


# --- nonlocal keyword ---
def outer():
    total = 0

    def inner():
        nonlocal total
        total += 1
        print("Inner total:", total)  # Inner total: 1

    inner()
    print("Outer total:", total)  # Outer total: 1

outer()


# --- Practical Use Case: Counter Closure ---
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
