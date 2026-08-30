import random
secret_number = random.randint(1,100)

guesses = 0

while guesses < 3:
    your_guess = int(input("What is your guess? "))
    guesses += 1
    if your_guess == secret_number:
        print("well done")
        break

if guesses == 3 and your_guess != secret_number:
    print(f"your answers were wrong the true answer is {secret_number}")
