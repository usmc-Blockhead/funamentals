def show_balance(balance):
    print("Current Balance: $" + str(balance))

def deposit(balance):
    amount = float(input("Enter the amount to Deposit: $"))
    return amount + balance

def withdrawl(balance):
    while True:
        amount = float(input("Enter the amount to Withdrawl: $"))
        if amount > balance:
            print("you're a Broke ass, try again")
        else:
            return balance - amount

def logout(name):
    print("Goodbye " + name + " !")
