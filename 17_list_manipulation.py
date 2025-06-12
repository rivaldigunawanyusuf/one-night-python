# 17 - List Manipulations (Slicing, Subsetting, Modifying)

# --- Basic Slicing ---
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4]) # [20, 30, 40]
print(numbers[:3]) # [10, 20, 30]
print(numbers[3:]) # [40, 50, 60]
print(numbers[-3:]) # [40, 50, 60]
print(numbers[:-2]) # [10, 20, 30, 40]
print(numbers[::2]) # [10, 30, 50]
print(numbers[::-1]) # [60, 50, 40, 30, 20, 10]

# Copying a list (shallow copy)
copy = numbers[:] 
print(copy) # [10, 20, 30, 40, 50, 60]

# --- Subsetting Lists (Nested or Indexed Access) ---
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[1]) # [3, 4]
print(nested[1][0]) # 3

# Mixed data types and indexing
data = [100, "text", True, [9, 8]]
print(data[3][1]) # 8

# --- List Manipulation (Mutating Methods) ---
fruits = ["apple", "banana", "cherry"]

fruits.append("orange") # Add to end
print(fruits) # ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "grape") # Insert at index 1
print(fruits) # ['apple', 'grape', 'banana', 'cherry', 'orange']

fruits.remove("banana") # Remove by value
print(fruits) # ['apple', 'grape', 'cherry', 'orange']

last = fruits.pop() # Remove last element
print(last) # orange
print(fruits) # ['apple', 'grape', 'cherry']

# Replace element by index
fruits[0] = "kiwi"
print(fruits) # ['kiwi', 'grape', 'cherry']

# Extend list with another list
fruits.extend(["melon", "berry"])
print(fruits) # ['kiwi', 'grape', 'cherry', 'melon', 'berry']

# Sorting and reversing
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers) # [1, 1, 3, 4, 5]

numbers.reverse()
print(numbers) # [5, 4, 3, 1, 1]

# Deleting elements
del numbers[2] # Remove by index
print(numbers) # [5, 4, 1, 1]

# Clear all elements
numbers.clear()
print(numbers) # []
