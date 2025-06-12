# 06 - f-Strings (Formatted String Literals)

name = "Alice"
age = 30

# Basic usage
print(f"My name is {name} and I am {age} years old.")  # My name is Alice and I am 30 years old.

# Expressions inside f-strings
print(f"In 5 years, I will be {age + 5} years old.")  # In 5 years, I will be 35 years old.

# Function call inside f-string
def square(n):
    return n * n

print(f"The square of 4 is {square(4)}")  # The square of 4 is 16

# Number formatting
pi = 3.1415926535
print(f"PI rounded to 2 decimals: {pi:.2f}")  # PI rounded to 2 decimals: 3.14
print(f"PI padded: {pi:10.2f}")  # PI padded:       3.14

# Thousands separator
salary = 1250000
print(f"Monthly salary: Rp {salary:,}")  # Monthly salary: Rp 1,250,000

# Conditional expressions
logged_in = True
print(f"Status: {'Logged in' if logged_in else 'Logged out'}")  # Status: Logged in

# Math inside f-strings
x = 10
y = 3
print(f"{x} * {y} = {x * y}")  # 10 * 3 = 30

# With string methods
language = "python"
print(f"{language.upper()} is awesome!")  # PYTHON is awesome!
