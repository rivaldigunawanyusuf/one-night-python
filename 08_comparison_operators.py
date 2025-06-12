# 08 - Comparison Operators (Conditional Checks)

# Equality and inequality
print(5 == 5)  # True
print(5 != 3)  # True
print(5 == "5")  # False (different types)

# Greater than / less than
print(10 > 5)  # True
print(2 < 1)  # False
print(5 >= 5)  # True
print(7 <= 8)  # True

# Comparing variables
a = 10
b = 20
print(a == b)  # False
print(a < b)  # True

# Comparing strings (lexicographically)
print("apple" < "banana")  # True
print("abc" == "ABC")  # False (case-sensitive)

# Caution with types
print(3 == 3.0)  # True (int and float are compared by value)
print(True == 1)  # True (bool is a subclass of int)
print(False == 0)  # True
