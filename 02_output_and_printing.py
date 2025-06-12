# 02 - Output & Printing

# Basic usage
print("Hello, Python!")

# Mixing types
print("Status:", True, "Score:", 87)

# Custom separator
print("apple", "banana", "cherry", sep=" | ")

# Custom ending
print("This is the first line.", end=" <-- no newline\n")  # Manual \n needed when using end param
print("This is the second line.")

# Print with formatted strings (f-strings)
name = "Alice"
age = 28
print(f"My name is {name}, and I am {age} years old.")
