import random
choices = ["rock", "paper", "scissors"]


player_score = 0
computer_score = 0

while player_score <2 and computer_score <2:
    computer_choice =random.choice(choices)
        
    your_choice = input("selct from; rock, paper, scissors").lower()
    while your_choice not in choices:
        print("try again")
        your_choice = input("selct from; rock, paper, scissors").lower()
    if your_choice == computer_choice:
        print("It's a draw!")
    elif your_choice == "rock" and computer_choice == "scissors":
        print(f"Player won round, computer chose {computer_choice}")
        player_score += 1
    elif your_choice == "paper" and computer_choice == "rock":
        print(f"Player won round, computer chose {computer_choice}")
        player_score += 1
    elif your_choice == "scissors" and computer_choice == "paper":
        print(f"Player won round, computer chose {computer_choice}")
        player_score += 1
    else:
        print(f"Player loses, computer chose {computer_choice}")
        computer_score += 1
if player_score == 2:
    print("Player has won")
else:
    print("player has lost")