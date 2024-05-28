winning_number=27#you can select any number
number =int(input("gueass a number between 1 to 100"))
if number==winning_number:
    print("you win the game")
else:
        if number>winning_number:
            print("too high")
        else:
            print("too lowr")