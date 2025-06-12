# 27 - Modules and Imports

# --- Importing Entire Module ---
import math

print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793

# --- Import Specific Attributes ---
from math import ceil, floor

print(ceil(4.2))       # 5
print(floor(4.8))      # 4

# --- Renaming on Import ---
import datetime as dt

now = dt.datetime.now()
print(now.year)        # e.g., 2025

# --- Import Custom Module (if you have another .py file in same folder) ---
# Assuming you have a file `helper.py` with a function `greet()`
# from helper import greet
# greet("Alice")

# --- __name__ == "__main__" check (used in modules) ---
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Python")    # This runs only if this file is executed directly
