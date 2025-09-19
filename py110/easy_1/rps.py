import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [paper, rock, scissors]

user_choice = int(input("What would you like to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
computer_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
    print("Invalid number. YOU LOSE!")
elif user_choice == 0 and computer_choice == 1:
    print("Your choice:")
    print(images[user_choice])
    print("My Choice:")
    print(images[computer_choice])
    print("You Win")
elif user_choice == 1 and computer_choice == 2:
    print("Your choice:")
    print(images[user_choice])
    print("My Choice:")
    print(images[computer_choice])
    print("You Win")
elif user_choice == 2 and computer_choice == 0:
    print("Your choice:")
    print(images[user_choice])
    print("My Choice:")
    print(images[computer_choice])
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("Your choice:")
    print(images[user_choice])
    print("My Choice:")
    print(images[computer_choice])
    print("I Win")
elif user_choice == 2 and computer_choice == 1:
    print("Your choice:")
    print(images[user_choice])
    print("My Choice:")
    print(images[computer_choice])
    print("I Win")
elif user_choice == 0 and computer_choice == 2:
    print("Your choice:")
    print(images[user_choice])
    print("My Choice:")
    print(images[computer_choice])
    print("I Win")
elif user_choice == computer_choice:
    print("Your choice:")
    print(images[user_choice])
    print("My Choice:")
    print(images[computer_choice])
    print("It's a draw!!")
