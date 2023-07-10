# Banking system

account_details = {234: 34550, 268: 122440, 212: 50100, 202: 71280, 276: 22490, 250: 233000, 292: 22222, 210: 334221,
                   281: 5524, 245: 2247}
login_details = {234: "123#", 268: "ABC!", 212: "1213*", 202: "dear6", 276: "smile@", 250: "happyme", 292: "555^",
                 210: "34567", 281: "90909", 245: "rider3"}


def main_welcome_screen():
    print(
        "1. Log into account\n"
        "2. Exit"
    )
    main_menu_selection = str(input())
    if main_menu_selection == "1":
        account_login()
    if main_menu_selection == "2":
        print("\n")
        print("Thank you for using Banking system!")
        exit()

    else:
        print("Select option 1 or 2")
        main_welcome_screen()


def account_login():
    print("Enter your account number:")
    global entered_account_number
    entered_account_number = int(input())

    print("Enter your password:")
    entered_password = input()

    if entered_account_number in login_details and login_details[entered_account_number] == entered_password:
        print("You have successfully logged in!")
        account_operations()

    else:
        print("\n")
        print("Wrong Account number or password!")
        print("\n")
        main_welcome_screen()


def account_operations():
    print(
        "A. Withdraw money\n"
        "B. Deposit money\n"
        "C. Logout"
    )
    selection = str(input()).upper()
    if selection == "A":
        withdraw_money()
    if selection == "B":
        deposit_money()
    if selection == "C":
        print("\n")
        main_welcome_screen()
    else:
        print("Select options A, B or C")
        account_operations()


def withdraw_money():
    print("\n")
    print("Account Balance :", account_details[entered_account_number])
    print("Enter amount to be withdrawn:")
    try:
        entered_withdraw_money = int(input())
    except ValueError:
        print("Invalid input")
        account_operations()
    else:
        if entered_withdraw_money <= account_details[entered_account_number]:
            print("Money withdrawn ")
            new_balance = account_details[entered_account_number] - entered_withdraw_money
            print("Account balance:", new_balance)
            account_details[entered_account_number] = new_balance
            account_operations()

        if int(entered_withdraw_money) > account_details[entered_account_number]:
            print("No sufficient Balance ")
            account_operations()


def deposit_money():
    print("\n")
    print("Account Balance :", account_details[entered_account_number])
    print("Enter amount to be deposited:")
    try:
        entered_deposit_money = int(input())
    except ValueError:
        print("Invalid input")
    else:
        new_balance = account_details[entered_account_number] + entered_deposit_money
        print("Account balance:", new_balance)
        account_details[entered_account_number] = new_balance
        print("\n")
        account_operations()


print(main_welcome_screen())
