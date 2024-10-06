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

game_images= [rock, paper, scissors]
import random


user_choice= int(input('What do you choose? "Rock" "Paper" or "Scissors"? "0" for Rock, "1" for Paper, "2" for Scissors\n'))
if user_choice>=3 or user_choice<0:
    print("You type an Invalide number. Please type again!")
print(game_images[user_choice])

computer_choice=random.randint(0,2)
print("Computer choice: ")
print(print(game_images[computer_choice]))

if user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice==2 and computer_choice==0:
    print("You lose!")
elif computer_choice>user_choice:
    print('You lose')
elif user_choice>computer_choice:
    print('You win!')
elif user_choice==computer_choice:
    print("It's a draw")
else:
    print("Invalid")
