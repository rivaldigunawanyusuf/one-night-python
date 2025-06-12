# 05 - Common String Methods

text = "  Python is Awesome!  "

# Convert to lowercase
print(text.lower())  # "  python is awesome!  "

# Convert to uppercase
print(text.upper())  # "  PYTHON IS AWESOME!  "

# Remove leading and trailing whitespaces
print(text.strip())  # "Python is Awesome!"

# Replace parts of the string
print(text.replace("Awesome", "Powerful"))  # "  Python is Powerful!  "

# Count substring occurrences
print(text.count("o"))  # 2

# Find the position of a substring
print(text.find("is"))  # 9

# Check if string starts or ends with a substring
print(text.startswith("  Python"))  # True
print(text.endswith("!  "))  # True

# Split into list by space
words = text.strip().split(" ")
print(words)  # ['Python', 'is', 'Awesome!']

# Join list into string
joined = "-".join(words)
print(joined)  # "Python-is-Awesome!"

# Capitalize first letter only
print("hello".capitalize())  # "Hello"

# Title case
print("python is great".title())  # "Python Is Great"

# Check if string is alphabetic, numeric, alphanumeric
print("Python3".isalnum())  # True
print("1234".isdigit())  # True
print("python".isalpha())  # True
