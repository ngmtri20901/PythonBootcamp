win = '''Congrats. You win\n
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")
choice1 = input('You\'re at a crossroad, where do you want to go? "Left" or "Right"\n').lower()

if choice1=="left":
    choice2= input('"You\'ve come to a lake. "Swim" or "Wait"\n').lower()
    if choice2=="wait":
        choice3= input('"You\'ve arrived at the treasure island. There is one room there, which door do you want to open? "Red", "Blue", or "Yellow"\n').lower()
        if choice3=="red":
            print("The room is full of fire. Game over\n")
        elif choice3=="blue":
            print("You fell into a sea. Game over\n")
        elif choice3=="yellow":
            print(win)
        else:
            print("You chose the door doesn't exists. Game over\n")
    else:
       print('You attacked by a crocodile. Game Over.\n') 
else:
    print('You fell into a hole. Game Over.\n')

