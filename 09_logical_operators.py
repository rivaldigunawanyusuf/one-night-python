# 09 - Logical Operators (Chained Conditionals)

# AND operator: both conditions must be True
print(True and True)  # True
print(True and False)  # False

a = 10
print(a > 5 and a < 20)  # True (both conditions are True)

# OR operator: at least one condition must be True
print(True or False)  # True
print(False or False)  # False

username = "admin"
password = "1234"
print(username == "admin" or username == "root")  # True

# NOT operator: reverses the boolean value
is_logged_in = False
print(not is_logged_in)  # True

# Combine with comparison
age = 25
has_ticket = True
print(age >= 18 and has_ticket)  # True

# Chain multiple logical conditions
x = 15
print(x > 10 and x < 20 and x != 13)  # True

# Mix AND, OR, and NOT
user = "guest"
access = False
print((user == "admin" or user == "guest") and not access)  # True
