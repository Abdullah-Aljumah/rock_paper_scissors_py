import random


def play():
    # User choise
    user = input("'R' for rock 'P' for paper 'S' for scissors: ").lower()

    # Make sure the user enter a valid value
    while user != "r" and user != "p" and user != "s":
        user = input(
            "'R' for rock 'P' for paper 's' for scissors: ").lower()

    # Computer choise
    computer = random.choice(['r', 'p', 's']).lower()

    # Translate
    user_choice = ""
    computer_choice = ""
    user_choice = "rock" if user == "r" else "paper" if user == "p" else "scissors"
    computer_choice = "rock" if computer == "r" else "paper" if computer == "p" else "scissors"

    # Show the user his choise and the comuter choise
    print("You choice is", user_choice)
    print("Computer choice is", computer_choice)

    # If it's a tie
    if user == computer:
        print("It's a tie!")

    # If the user won
    elif (user_win(user, computer)):
        print("You won!")
    # If the comuter won
    else:
        print('You lost!')


# function check if the user won
def user_win(user, computer):
    if (user == 'r' and computer == 's' or user == 'p' and computer == 'r' or user == 's' and computer == 'p'):
        return True


play()
