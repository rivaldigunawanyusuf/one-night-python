# 25 - Lambda

# --- Basic Lambda ---
add = lambda x, y: x + y
print(add(3, 5))           # 8

# Lambda used directly
print((lambda x: x * 2)(4))  # 8

# --- With Built-in Functions ---

# Using lambda with sorted()
names = ['alice', 'Bob', 'dave']
sorted_names = sorted(names, key=lambda name: name.lower())
print(sorted_names)       # ['alice', 'Bob', 'dave']

# Using lambda with map()
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)            # [1, 4, 9, 16]

# Using lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)              # [2, 4]

# --- Returning Functions (for closures) ---
def multiplier(factor):
    return lambda x: x * factor

double = multiplier(2)
print(double(10))         # 20

# Lambda for sorting complex structures
products = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Phone', 'price': 800},
    {'name': 'Tablet', 'price': 600}
]

# Sort by price
products_sorted = sorted(products, key=lambda item: item['price'])
print(products_sorted)    # Sorted by price ascending

# --- Notes ---
# Lambdas are anonymous (unnamed) functions.
# They're useful for short, inline functions.
# Best used when a full function with def would be unnecessarily verbose.
