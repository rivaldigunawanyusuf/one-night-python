# 25 - Boolean Context & Truthy / Falsy Values

# --- Truthy and Falsy Values ---

# Falsy values in Python:
# - False
# - None
# - 0, 0.0
# - "", ''
# - [], {}, (), set()
# - range(0)

# Everything else is considered Truthy

print(bool(False))      # False
print(bool(None))       # False
print(bool(0))          # False
print(bool(""))         # False
print(bool([]))         # False
print(bool({}))         # False
print(bool(()))         # False
print(bool(range(0)))   # False

# Truthy examples
print(bool(123))        # True
print(bool("hello"))    # True
print(bool([1, 2]))     # True

# --- Boolean Contexts in Control Flow ---

value = []
if value:
    print("This is truthy")
else:
    print("This is falsy")       # This is falsy

text = "Python"
if text:
    print("Has content")         # Has content

# --- Use Case: Short-Circuit Evaluation ---

username = input("Enter username: ") or "guest"
print("Welcome,", username)
# If user enters nothing, "guest" is used by default

# --- Use Case: While Loops ---

items = [1, 2, 3]
while items:
    print(items.pop())           # 3, 2, 1

# Empty list is falsy, loop stops when list is empty

# --- Use Case: Simplifying Conditions ---

# Instead of:
# if len(data) > 0:
#     ...

# Use:
# if data:
#     ...
