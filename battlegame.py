# characters
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
end = "Exit"

# hit points
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 225


# damage
wizard_damage = 120
elf_damage = 100
human_damage = 20
orc_damage = 140


# input
while True:
    dragon_hp = 300
    dragon_damage = 50
    while True:
        print("1) " + wizard)
        print("2) " + elf)
        print("3) " + human)
        print("4) " + orc)
        print("5) " + end)
        choice = input("Choose your character:")
        choice = choice.lower()

        if choice == "1" or choice == "wizard":
            choice = "wizard"
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if choice == "2" or choice == "elf":
            choice = "elf"
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if choice == "3" or choice == "human":
            choice = human
            my_hp = human_hp
            my_damage = human_damage
            break
        if choice == "4" or choice == "orc":
            choice = "orc"
            my_hp = orc_hp
            my_damage = orc_damage
            break
        if choice == "5" or choice == "exit":
            print("Thank you for playing")
            exit()
        else:
            print("Unknown Character")

    print("You have chosen", choice)
    print("Damage:", my_damage)
    print("Health:", my_hp)
    print(" ")

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", choice, "damaged the Dragon!")
        print("The Dragon's hit-points are now:", dragon_hp)
        print("")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break

        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back at", choice)
        print("The", choice, "hit-points are now:", my_hp)
        print("")
        if my_hp <= 0:
            print("The ", choice, "has lost the battle")
            break

    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "n":
        break
    elif play_again.lower() == "y":
        continue
