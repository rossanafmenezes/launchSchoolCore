import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def winner(player_choice, computer_choice):
    win_conditions = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    if player_choice == computer_choice:
        return "It's a tie!"

    if computer_choice in win_conditions[player_choice]:
        return 'You win!'
    else:
        return 'Computer Wins!'

def prompt(message):
    print(f'==> {message}')

prompt('Welcome to RSP! Please make your choice:')

computer_score = 0
player_score = 0

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().lower()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input().lower()

    computer_choice = random.choice(VALID_CHOICES)

    result = winner(choice, computer_choice)

    prompt(f'You chose: {choice}, the Computer chose: {computer_choice}')
    print(result)

    if result == 'Computer Wins!':
        computer_score += 1
    elif result == 'You win!':
        player_score += 1

    prompt(
        f'The current score is: You {player_score} x {computer_score} Computer'
        )

    if computer_score == 3:
        prompt('GGWP! But the computer won!!')
        break
    if player_score == 3:
        prompt('GGWP! You are the big winner!!')
        break
