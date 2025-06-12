# 10 - Control Flow: if, elif, else

age = 18

# Basic if condition
if age >= 18:
    print("You are an adult.")  # condition is True

# if with else
if age < 18:
    print("You are underage.")
else:
    print("Access granted.")  # age is not less than 18

# if, elif, else chain
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")  # this block runs
else:
    print("Grade: D or below")

# Multiple conditions
username = "admin"
logged_in = True

if username == "admin" and logged_in:
    print("Welcome back, admin!")  # both conditions are True
else:
    print("Access denied.")

# Nested if example
x = 5
if x > 0:
    if x < 10:
        print("x is a positive single-digit number.")  # nested condition
