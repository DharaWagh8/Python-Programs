import random

winning_number=random.randint(1,100)
#winning_number=int(winning_number)
guess_number=1
n=int(input("guess a number between 1 to 100: "))
game_over=False
while not game_over:
    
    if n==winning_number:
        print(f"you win!!! and you gussed this number in {guess_number} times")
        game_over=True
    else:
        if n>winning_number:
            print(f"too high")
        elif n<winning_number:
            print(f"too low")
        
    guess_number+=1
    n=int(input("guess again"))
            

