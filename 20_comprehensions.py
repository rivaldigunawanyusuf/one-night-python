# 20 - Comprehensions

# --- List Comprehension ---
squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
print(squares)

# With condition
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
print(evens)

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)] # ['even', 'odd', 'even', 'odd', 'even']
print(labels)

# Nested comprehension
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix) # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten 2D list
flattened = [num for row in matrix for num in row]
print(flattened) # [0, 0, 0, 0, 1, 2, 0, 2, 4]

# --- Dictionary Comprehension ---
squared_dict = {x: x**2 for x in range(5)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(squared_dict)

# Conditional dict comprehension
filtered_dict = {x: x**2 for x in range(10) if x % 2 == 0} # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
print(filtered_dict)

# --- Set Comprehension ---
unique_lengths = {len(word) for word in ["hi", "hello", "world", "hi"]} # {2, 5}
print(unique_lengths)

# --- Equivalent with loop ---
squares_loop = []
for x in range(5):
    squares_loop.append(x**2)
print(squares_loop) # [0, 1, 4, 9, 16]
