# 04 - Arithmetic Operators

a = 15
b = 4

# Addition
result = a + b
print(f"{a} + {b} = {result}") # 19

# Subtraction
result = a - b
print(f"{a} - {b} = {result}") # 11

# Multiplication
result = a * b
print(f"{a} * {b} = {result}") # 60

# Division (always returns float)
result = a / b
print(f"{a} / {b} = {result}") # 3.75

# Floor Division (returns integer result)
result = a // b
print(f"{a} // {b} = {result}") # 3

# Modulus (remainder)
result = a % b
print(f"{a} % {b} = {result}") # 3

# Exponentiation (power)
result = a ** b
print(f"{a} ** {b} = {result}") # 50625

# Mixing with float
c = 2.5
print(f"{a} + {c} = {a + c}") # 17.5

# Operator precedence (PEMDAS)
result = a + b * 2 # multiplication happens before addition
print(f"{a} + {b} * 2 = {result}") # 15 + 8 = 23
