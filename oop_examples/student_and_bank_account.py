class Student:
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display_info(self):
        print(f"Name: {self.name}. Age: {self.age}. CGPA: {self.cgpa}")

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount must be positive.")
            return
        
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return
        
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def check_balance(self):
        print(f"Current balance is {self.balance}.")

def main():
    a = Student("Olu", 18, 4.83)
    b = Student("Boma", 21, 4.85)

    a.display_info()
    b.display_info()


    c = BankAccount("Olu", "4061330410", 1000000)
    c.deposit(100000)
    c.withdraw(5683.19)
    c.check_balance()

main()