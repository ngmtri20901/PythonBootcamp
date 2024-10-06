import random as rd

# Get names from user input
names_string = input("Enter names separated by commas: ")  # Prompt the user for input

names = names_string.split(", ")

num_items = len(names)

random_choice = rd.randint(0, num_items - 1)

person = names[random_choice]

# Print who will pay the bill
print(f"{person} will pay the bill")
