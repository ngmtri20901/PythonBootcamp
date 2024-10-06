import random

# 1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list

from hangman_art import logo
print(logo)

correct_answer= random.choice(word_list)
word_length= len(correct_answer)

dash = []
for i in range(word_length):
    dash.append("_")

lives = 6

end_game=False

while not end_game and lives>0:
    user_input= input("Enter your guess: ")
    for position in range(word_length):
        #loop letter=0 -> end
        letter=correct_answer[position]
        if letter==user_input:
            dash[position]=user_input
        
    if user_input not in correct_answer:
        lives -= 1  # Reduce lives on incorrect guess
        print(f"Incorrect guess. You have {lives} lives left.")
        if lives==0:
            end_game=True
            print("End of life. You lost")
    
    print(" ".join(dash))  # Show current state of the word

    if "_" not in dash:
        end_game = True
        print("You win!")
    elif lives == 0:
        print("You lost!")

    from hangman_art import stages
    print(stages[lives])

print(f"Correct answer is: {correct_answer}")