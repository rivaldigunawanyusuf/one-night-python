# 07 - Getting User Input

# Basic input (always returns string)
name = input("What is your name? ")  # prompt the user
print(f"Hello, {name}!")  # use f-string to respond

# Input with conversion
age = input("How old are you? ")  # user input is a string
print(f"You said you're {age} years old.")  # no type conversion yet

# Convert input to integer
age = int(age)  # string to integer
print(f"In 5 years, you will be {age + 5} years old.")  # arithmetic after conversion

# Combine input and string method
city = input("Where are you from? ").strip().title()
print(f"Nice! I've heard {city} is beautiful.")  # standardized formatting

# Float input example
height = float(input("Enter your height in meters: "))
print(f"Your height is {height:.2f} meters.")  # formatted output
