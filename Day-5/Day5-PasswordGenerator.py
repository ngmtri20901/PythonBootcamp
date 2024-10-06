#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))  
    for char in range(1, nr_symbols + 1):
        password_list.append(random.choice(symbols))  
    for char in range(1, nr_numbers + 1):
        password_list.append(random.choice(numbers)) 

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    return password

def main():
    print("Welcome to the PyPassword Generator!")
    
    while True:
        password = generate_password()
        
        if len(password) < 8:
            choice = input('It\'s recommended that a password should contain at least 8 characters. Do you want to generate a new password? Type "Y" for Yes or "N" for No: ').lower()
            
            if choice == "n":
                print(f"Your password is {password}")
                break
            elif choice == "y":
                print("Generating a new password...")
                continue
            else:
                print("Invalid input. Please try again.")
        else:
            print(f"Your password is {password}")
            break

main()
