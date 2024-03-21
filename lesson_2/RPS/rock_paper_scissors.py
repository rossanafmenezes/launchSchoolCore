import random


VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']


def winner(player_choice, computer_choice):
    if ((player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "spock" and computer_choice == "rock") or
        (player_choice == "paper" and computer_choice == "spock") or
        (player_choice == "lizard" and computer_choice == "paper") or
        (player_choice == "scissors" and computer_choice == "lizard") or
        (player_choice == "spock" and computer_choice == "scissors") or
        (player_choice == "lizard" and computer_choice == "spock") or
        (player_choice == "rock" and computer_choice == "lizard") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")):
        prompt("You win!")
    elif player_choice == computer_choice :
        prompt("It's a tie!")
    else:
        prompt("Computer Wins")

def prompt(message):
    print(f'==> {message}')

while True:
    prompt('Welcome to RSP! Please make your choice:')
    prompt(f'{", ".join(VALID_CHOICES)}')
    choice = input().lower()

    while choice not in VALID_CHOICES:
        prompt('This is not a valid option. Try again')
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose: {choice}, the Computer chose: {computer_choice}')
    winner(choice, computer_choice)

    prompt('Would you like to play again (y/n)?')
    answer = input().lower()
    while True: 
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("Please enter 'y' or 'n'. ")
        answer = input().lower()
    if answer[0] == 'n':
        break