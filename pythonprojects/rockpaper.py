import random
choices = ["rock", "paper", "scissors"]

computer_choice =random.choice(choices)

player_score = 0
computer_score = 0


your_choice = input("selct from; rock, paper, scissors").lower()
while your_choice not in choices:
    print("try again")
    your_choice = input("selct from; rock, paper, scissors").lower()


if your_choice == computer_choice:
    print("It's a draw!")
elif your_choice == "rock" and computer_choice == "scissors":
    print(f"Player wins, computer chose {computer_choice}")
elif your_choice == "paper" and computer_choice == "rock":
    print(f"Player wins, computer chose {computer_choice}")
elif your_choice == "scissors" and computer_choice == "paper":
    print(f"Player wins, computer chose {computer_choice}")
else:
    print(f"Player loses, computer chose {computer_choice}")