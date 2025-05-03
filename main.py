from bank_account import BankAccount

user_id = input("Enter your user ID: ")
account = BankAccount(user_id)
account.create_account()

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1–4): ")

    if choice == '1':
        balance = account.get_balance()
        print(f"Your current balance is: ${balance:.2f}")

    elif choice == '2':
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be positive.")
            else:
                account.deposit(amount)
                print(f"${amount:.2f} deposited successfully.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    elif choice == '3':
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be positive.")
            else:
                try:
                    account.withdraw(amount)
                    print(f"${amount:.2f} withdrawn successfully.")
                except ValueError as e:
                    print(e)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
