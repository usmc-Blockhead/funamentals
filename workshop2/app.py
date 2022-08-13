from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")

while True:
    name = input("Enter Username to register: ")
    if not name.isalpha():
        print("Please enter characters A-Z only")
    elif len(name) > 10:
        print("Please keep Username to less than 10 letters")
    else:
        break
while True:
    pin = input("Please enter PIN: ")
    if not pin.isdigit():
        print("Please enter Numbers only")
    elif len(pin) != 4:
        print("Please set Pin to 4 numbers")
    else:
        break

balance = 0.0

print(name + " has been registered with starting balance of: $" + str(balance))

while True:
    print("LOGIN:")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter pin: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful")
        break
    else:
        print("Invaild Credentials!")

while True:
    atm_menu(name)
    option = input("Enter option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdrawl(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
