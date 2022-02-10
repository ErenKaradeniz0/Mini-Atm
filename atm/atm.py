#Mini-Atm program by wiserenn

FirstAccount = {
    'name': input("Please enter your name : "),
    "accountid": '12465496',
    "balance": int(input("Enter first account's main balance : ")),
    'additionalaccountbalance': int(input("Enter first account's additional account balance : ")),
}

SecondAccount = {
    'name': input("Please enter your  second account name : "),
    "accountid": '12465497',
    "balance": int(input("Enter second account's main  balance : ")),
    'additionalaccountbalance': int(input("Enter second account's additional account balance : ")),
}


def withdraw(account, amount):
    if amount > 0:
        if account["balance"] >= amount:
            account["balance"] -= amount
            print(f'You have withdrawn {amount} TL.')
            checkbalance(account)
        else:
            total = account["balance"] + account['additionalaccountbalance']
            if total >= amount:
                useofadditionalaccount = (input(f'The amount you want to withdraw : "{amount}"'
                                                f'exceeds your main account limit. '
                                                f'Do you want to use your additional account : (yes/no) ').lower())
                if useofadditionalaccount == 'yes':
                    amountwithdrawinaddaccount = amount - account["balance"]
                    account["balance"] = 0
                    account['additionalaccountbalance'] -= amountwithdrawinaddaccount
                    print(f'You have withdrawn {amount} TL.')
                    checkbalance(account)
                elif useofadditionalaccount == "no":
                    print("You do not using your additional account...")
                    checkbalance(account)
                else:
                    print("You have entered invalid character")
                    checkbalance(account)
            else:
                print("Sorry, insufficient balance")
                checkbalance(account)
    else:
        print("Please enter valid/positive value")


def deposit(account, amount):
    if amount > 0:
        print("Do you want to deposit your money into the main account or additional account?")
        choice = (input("for main account : main for additional account add  :  main/add ").lower())
        if choice == "main":
            account["balance"] += amount
        elif choice == "add":
            account["additionalaccountbalance"] += amount
        else:
            print("You have entered invalid character")
        checkbalance(account)
    else:
        print("Please enter valid/positive value")


def checkbalance(account):
    print(
        f"Hello {account['name']} : In your account with id : {account['accountid']} You have {account['balance']} TL. "
        f"In you additional account you have : {account['additionalaccountbalance']} TL")


accountname = input(f"Please enter account :{FirstAccount['name']}  / {SecondAccount['name']} ").lower()
if accountname == FirstAccount['name']:
    changes = int(input("Please enter number of operations you want :"))
    while 0 < changes:
        operation = input("Please enter operation withdraw /deposit / checkbalance :").lower()
        changes -= 1
        if operation == "withdraw":
            checkbalance(FirstAccount)
            withdraw(FirstAccount, int(input("Please enter the amount you want to withdraw :")))
        elif operation == "deposit":
            checkbalance(FirstAccount)
            deposit(FirstAccount, int(input("Please enter the amount you want to deposit :")))
        elif operation == "checkbalance":
            checkbalance(FirstAccount)
        else:
            print("You have entered invalid operation")
elif accountname == SecondAccount['name']:
    changes = int(input("Please enter number of operations you want : "))
    while 0 < changes:
        operation = input("Please enter operation withdraw / deposit/ checkbalance : ").lower()
        changes -= 1
        if operation == "withdraw":
            checkbalance(SecondAccount)
            withdraw(SecondAccount, int(input("Please enter the amount you want to withdraw :")))
        elif operation == "deposit":
            checkbalance(SecondAccount)
            deposit(SecondAccount, int(input("Please enter the amount you want to deposit :")))
        elif operation == "checkbalance":
            checkbalance(SecondAccount)
        else:
            print("You have entered invalid operation")
else:
    print("please enter valid account name")
