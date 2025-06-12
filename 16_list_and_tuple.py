# 16 - Lists and Tuples

# LIST: Mutable, ordered, can hold mixed types
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple

fruits[1] = "mango"  # Lists are mutable
print(fruits)  # ['apple', 'mango', 'cherry']

fruits.append("orange")  # Add to the end
print(fruits)

fruits.remove("apple")  # Remove by value
print(fruits)

# Can contain mixed types
data = [42, "hello", True, 3.14]
print(data)

# Nested lists
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3

# TUPLE: Immutable, ordered, can hold mixed types
point = (4, 5)
print(point[0])  # 4

# Tuples are immutable (cannot be changed)
# point[0] = 10  # This will raise TypeError

# Singleton tuple must have a comma
single = (42,)
print(type(single))  # <class 'tuple'>

# Tuple unpacking
x, y = point
print(f"x = {x}, y = {y}")

# List vs Tuple: When to use
# Use list if data will change
# Use tuple if data is fixed or used as dictionary keys

# List methods
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5]

numbers.reverse()
print(numbers)  # [5, 4, 3, 1, 1]

# Tuple can be used for fast iteration and safety
coords = [(0, 0), (1, 2), (2, 4)]
for x, y in coords:
    print(f"x: {x}, y: {y}")
