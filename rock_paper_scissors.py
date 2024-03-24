import random

user_wins = 0
comp_wins = 0
draw = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type (Rock/Paper/Scissor) or Q to quit:").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_num = random.randrange(0,3)

    computer_pick = options[random_num]
    print("Computer Picked",computer_pick)

    if user_input == "rock" and computer_pick == "scissor":
        print("You win")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You win")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw")
        draw += 1    
    else:
        print("Computer Wins")
        comp_wins += 1

print("You won", user_wins, "times")
print("Computer won", comp_wins, "times")
print("Draw",draw)
print("Goodbye")