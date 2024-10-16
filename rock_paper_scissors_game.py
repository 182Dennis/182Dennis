import random
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
computer_input = random.randint(0, 2)
options = ["Rock", "Paper", "Scissors"]
print(f"You chose {options[player_input]}")
print(f"The computer chose {options[computer_input]}")

if player_input == 0 and computer_input == 2:
    print("You win!")
elif computer_input == 0 and player_input == 2:
    print("You lose!")
elif computer_input > player_input:
    print("You lose!")
elif player_input > computer_input :
    print("You win!")
elif computer_input == player_input:
    print("It is a draw!")



