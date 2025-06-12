# 15 - range()

# Basic usage
print(list(range(5)))  # [0, 1, 2, 3, 4]

# Range with start and stop
print(list(range(1, 6)))  # [1, 2, 3, 4, 5]

# Range with step
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

# Negative step (counting down)
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

# Using range in a loop
for i in range(3):
    print("Iteration", i)

# Caution: range is exclusive on the end
print(list(range(1, 10)))  # ends at 9, not 10

# Empty range (stop is less than start with positive step)
print(list(range(5, 2)))  # []

# Range with negative step but wrong direction
print(list(range(1, 5, -1)))  # [] (step is negative, but start < stop)

# Range can be converted to list, tuple, etc.
print(tuple(range(3)))  # (0, 1, 2)

# Using range with len()
names = ["Alice", "Bob", "Charlie"]
for i in range(len(names)):
    print(i, names[i])

# Looping backwards using reversed() and range
for i in reversed(range(5)):
    print(i)

# Range + zip example
questions = ["Name?", "Age?", "Country?"]
answers = ["Alice", "24", "USA"]
for i, (q, a) in enumerate(zip(questions, answers)):
    print(f"Q{i+1}: {q} → {a}")
