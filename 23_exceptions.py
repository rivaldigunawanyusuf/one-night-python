# 23 - Exceptions and Handling

# --- Basic Try-Except ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")  # Cannot divide by zero.

# --- Catching Multiple Exceptions ---
try:
    num = int("abc")
    result = 10 / num
except ValueError:
    print("Invalid conversion to integer.")  # Invalid conversion to integer.
except ZeroDivisionError:
    print("Cannot divide by zero.")

# --- Generic Exception Handler ---
try:
    x = undefined_variable
except Exception as e:
    print("An error occurred:", e)  # An error occurred: name 'undefined_variable' is not defined

# --- Try-Except-Else ---
try:
    value = 42
except Exception:
    print("Something went wrong.")
else:
    print("No error occurred.")  # No error occurred.

# --- Try-Finally ---
try:
    print("Doing something important")
finally:
    print("Cleanup code always runs")  # Cleanup code always runs

# --- Full Try-Except-Else-Finally Pattern ---
try:
    f = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")  # File not found.
else:
    content = f.read()
    print(content)
    f.close()
finally:
    print("Execution completed.")  # Execution completed.

# --- Raising Exceptions Manually ---
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b

try:
    print(divide(5, 0))
except ValueError as e:
    print("Custom Error:", e)  # Custom Error: b cannot be zero
