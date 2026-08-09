def check_balance(balance):
    return f"\nYour balance is: ${balance}"

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"\n${amount} deposited successfully.")
    else:
        print("\nYou can't deposit a negative amount.")
    return balance

def withdraw(balance, amount):
    if 0 < amount <= balance:
        balance -= amount
        print(f"\n${amount} withdrawn successfully.")
    elif amount > balance:
        print("\nInsufficient funds.")
    else:
        print("\nYou can't withdraw a negative amount")
    return balance

balance = 1000

while True:
    print("\n--- Welcome to ATM ---")

    option = input("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\n\n Choose an option: ")

    if option == '1':
        print(check_balance(balance))
    elif option == '2':
        amount = int(input("\nEnter deposit amount: "))
        balance = deposit(balance, amount)
    elif option == '3':
        amount = int(input("\nEnter withdrawal amount: "))
        balance = withdraw(balance, amount)
    elif option == '4':
        break
    else:
        print("\nInvalid option!")
        