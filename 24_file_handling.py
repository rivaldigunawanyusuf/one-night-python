# 24 - File Handling (Reading and Writing Files)

# --- Writing to a File ---
with open("example.txt", "w") as f:
    f.write("Hello World\n")
    f.write("This is Python.\n")

# --- Reading Entire File ---
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # Hello World\nThis is Python.

# --- Reading Line by Line ---
with open("example.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())  # Line: Hello World ...

# --- Appending to a File ---
with open("example.txt", "a") as f:
    f.write("Another line.\n")

# --- Reading Lines into a List ---
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['Hello World\n', 'This is Python.\n', 'Another line.\n']

# --- Writing from a List ---
lines_to_write = ["Line A\n", "Line B\n"]
with open("example2.txt", "w") as f:
    f.writelines(lines_to_write)

# --- Using try-except when dealing with files ---
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist.")  # File does not exist.
