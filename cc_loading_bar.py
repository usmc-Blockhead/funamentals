for amount_loaded in range(0, 101, 5):
    if amount_loaded == 25:
        print(amount_loaded)
        print("You are 1/4 of the way")
    elif amount_loaded == 50:
        print(amount_loaded)
        print("You are 1/2 of the way")
    elif amount_loaded == 75:
        print(amount_loaded)
        print("You are 3/4 of the way")
    elif amount_loaded == 100:
        print(amount_loaded)
        print("You are ALL of the way")
    else:
        print(amount_loaded)