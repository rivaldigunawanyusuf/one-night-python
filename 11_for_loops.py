# 11 - For Loops

# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # prints each item in the list

# Looping over a string
for char in "hello":
    print(char)  # prints each character

# Using range() in a loop
for i in range(5):
    print(i)  # prints 0 to 4

# Specifying start and stop in range
for i in range(2, 6):
    print(i)  # prints 2 to 5

# Using step in range
for i in range(0, 10, 2):
    print(i)  # prints 0, 2, 4, 6, 8

# Using enumerate() to get index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(index, color)  # prints index and value

# Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)  # multiplication table
