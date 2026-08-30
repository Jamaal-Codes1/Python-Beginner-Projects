import random
choices = ["rock", "paper", "scissors"]

computer_choice =random.choice(choices)

your_choice = input("selct from; rock, paper, scissors")

if your_choice == computer_choice:
    print("It's a draw!")