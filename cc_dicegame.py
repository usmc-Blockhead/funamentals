import random

high_score = 0


def dice_game():
    global high_score

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print("Current High Score: ", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
    choice = input("Make a Choice: ").lower()

    while True:
        if choice == "1" or choice == "roll" or choice == "roll dice":
            print("you rolled a ...", die1)
            print("you rolled a ...", die2)

            print("you have rolled a total of: ", die1 + die2)

            if die1 + die2 > high_score:
                high_score = die1 + die2
                print("New High Score!")
            break

        if choice == "2" or choice == "Leave Game":
            print("Thank you for playing")
            exit()
        else:
            dice_game()
    dice_game()

dice_game()
