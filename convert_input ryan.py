total_cash = 0


while True:
    user_input = input('Enter amount to transfer: $ ')
    user_input =
     float(user_input)
    if user_input < 101 and user_input > 0:

        total_cash = total_cash + float(user_input)
        print('Total cash is now: $')
        print(total_cash)
        break
    else:
        print('not valid')
