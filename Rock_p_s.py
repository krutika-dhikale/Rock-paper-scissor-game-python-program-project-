import random

ans = 'yes'

while ans == 'yes':
    print("***** ROCK PAPER SCISSOR GAME *****")

    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)

    user = input("Enter rock, paper or scissor: ").lower()

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif user == "rock" and computer == "scissor":
        print("You Win!")

    elif user == "paper" and computer == "rock":
        print("You Win!")

    elif user == "scissor" and computer == "paper":
        print("You Win!")

    elif user in choices:
        print("Computer Wins!")

    else:
        print("Invalid Input")

    ans = input("Do you want to play again? (yes/no): ").lower()

print("Thanks for playing!")