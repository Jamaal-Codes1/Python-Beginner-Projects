import random
choices = ["rock", "paper", "scissors"]

computer_choice =random.choice(choices)

your_choice = input("selct from; rock, paper, scissors")

if your_choice == computer_choice:
    print("It's a draw!")
elif your_choice == "rock" and computer_choice == "scissors":
    print("Player wins")
elif your_choice == "paper" and computer_choice == "rock":
    print("Player wins")
elif your_choice == "scissors" and computer_choice == "paper":
    print("Player wins")
else:
    print("Player loses")
