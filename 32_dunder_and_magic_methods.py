# 32 - Dunder and Magic Methods

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} - {self.pages} pages"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages


# --- Usage ---
b1 = Book("Book One", 300)
b2 = Book("Book Two", 300)
b3 = Book("Book Three", 150)

print(b1)            # Book One - 300 pages
print(len(b1))       # 300
print(b1 == b2)      # True
print(b1 == b3)      # False
