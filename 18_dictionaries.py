# 18 - Dictionaries

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person) # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing values
print(person["name"]) # Alice
print(person.get("age")) # 30

# Modifying values
person["age"] = 31
print(person) # {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Adding a new key-value pair
person["email"] = "alice@example.com"
print(person) # {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# Removing a key-value pair
del person["city"]
print(person) # {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

# Using pop() method
email = person.pop("email")
print(email) # alice@example.com
print(person) # {'name': 'Alice', 'age': 31}

# Checking for existence of keys
print("name" in person) # True
print("city" in person) # False

# Looping through dictionary
for key in person:
    print(key, person[key]) # name Alice \n age 31

# Looping with items()
for key, value in person.items():
    print(f"{key}: {value}") # name: Alice \n age: 31

# Nested dictionary
people = {
    "alice": {"age": 30, "email": "alice@example.com"},
    "bob": {"age": 25, "email": "bob@example.com"}
}
print(people["bob"]["email"]) # bob@example.com
