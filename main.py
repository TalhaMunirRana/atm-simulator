balance = 1000

while True:
    print("\n--- Welcome to ATM ---")

    option = input("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\n\n Choose an option: ")

    if option == '1':
        print(f"\nYour balance is: ${balance}")
    elif option == '2':
        amount = int(input("\nEnter deposit amount: "))
        balance += amount
        print(f"\n${amount} deposited successfully.")
    elif option == '3':
        amount = int(input("\nEnter withdrawal amount: "))
        balance -= amount
        print(f"\n${amount} withdrawn successfully.")
    elif option == '4':
        break
    else:
        print("\nInvalid option!")
        