# 19 - Sets

# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits) # {'apple', 'banana', 'cherry'}

# Sets automatically remove duplicates
numbers = {1, 2, 2, 3, 4, 4}
print(numbers) # {1, 2, 3, 4}

# Add an element
fruits.add("orange")
print(fruits) # {'apple', 'banana', 'cherry', 'orange'}

# Remove an element
fruits.remove("banana")
print(fruits) # {'apple', 'cherry', 'orange'}

# Discard does not raise error if element doesn't exist
fruits.discard("banana")
print(fruits) # {'apple', 'cherry', 'orange'}

# Pop removes a random element
removed = fruits.pop()
print(removed) # (random fruit)
print(fruits) # remaining elements

# Clear all elements
fruits.clear()
print(fruits) # set()

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b)) # {1, 2, 3, 4, 5}
print(a | b) # {1, 2, 3, 4, 5}

print(a.intersection(b)) # {3}
print(a & b) # {3}

print(a.difference(b)) # {1, 2}
print(a - b) # {1, 2}

print(a.symmetric_difference(b)) # {1, 2, 4, 5}
print(a ^ b) # {1, 2, 4, 5}

# Membership test
print(2 in a) # True
print(5 in a) # False
