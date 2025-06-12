# 14 - Built-in Functions

# abs() - absolute value
print(abs(-10))  # 10

# len() - length of string, list, etc.
print(len("hello"))  # 5
print(len([1, 2, 3]))  # 3

# max() - maximum value
print(max(5, 9, 3))  # 9

# min() - minimum value
print(min(5, 9, 3))  # 3

# sum() - sum of items in iterable
print(sum([1, 2, 3, 4]))  # 10

# round() - rounding a number
print(round(3.14159, 2))  # 3.14

# type() - type of a value
print(type("text"))  # <class 'str'>
print(type(10))  # <class 'int'>

# str(), int(), float() - type casting
print(str(100))  # "100"
print(int("50"))  # 50
print(float("3.14"))  # 3.14

# sorted() - returns a sorted list
print(sorted([5, 2, 9, 1]))  # [1, 2, 5, 9]

# reversed() - returns an iterator (needs to be converted)
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# zip() - combines two or more iterables
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(name, "scored", score)

# enumerate() - adds index to iterable
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(index, color)

# range() - generates a sequence of numbers
print(list(range(1, 6)))  # [1, 2, 3, 4, 5]
