class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


# Create object
acc = BankAccount(5000)

acc.deposit(1000)
acc.withdraw(2000)

print("Current Balance:", acc.get_balance())