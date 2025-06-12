# 03 - Variables

# Variable assignment
username = "admin"
user_age = 30
is_logged_in = True

print("Username:", username)
print("Age:", user_age)
print("Login status:", is_logged_in)

# Python is dynamically typed
x = 10 # initially int
print("x =", x, "| type:", type(x))

x = "Ten" # now str
print("x =", x, "| type:", type(x))

# Variable naming conventions (PEP 8)
# - Use snake_case for variables
# - Use descriptive names

first_name = "Alice"
total_amount = 99.99

# Constants (by convention — Python doesn't enforce them)
PI = 3.14159
MAX_USERS = 100

# Swapping values
a, b = 1, 2
a, b = b, a
print("a:", a, "| b:", b)

# Multiple assignments
width, height, color = 1920, 1080, "blue"
print("Resolution:", width, "x", height, "| Color:", color)

# Invalid variable names:
# Variable names cannot start with a number, contain spaces, or use special characters (except _)
# For example:
# 2fast = "nope"        # SyntaxError
# user-name = "invalid" # SyntaxError
# total$amount = 100    # SyntaxError

# Valid alternative:
fast2 = "yes"
user_name = "valid"
total_amount = 100
