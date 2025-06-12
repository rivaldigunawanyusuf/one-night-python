# 31 - Encapsulation and @property

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# --- Using @property to access private data more Pythonically ---
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # protected by convention

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9


# --- Usage Example ---
acct = BankAccount("Alice", 1000)
acct.deposit(500)
acct.withdraw(300)
print(acct.get_balance())  # 1200

temp = Temperature(25)
print(temp.fahrenheit)     # 77.0
temp.fahrenheit = 86
print(temp._celsius)       # 30.0
