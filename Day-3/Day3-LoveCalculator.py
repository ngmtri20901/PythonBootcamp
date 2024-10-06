print("The Love Calculator is calculating your score...")
name_1= input("Enter first name\n")
name_2= input("Enter second name\n")
combined_name= name_1 + name_2
lower= combined_name.lower()
#for i in lower - if lower[i] == 't' TRUE= TRUE + 1, i++
TRUE= 0
LOVE=0

for char in lower:
    if char in ['t','r','u','e']:
        TRUE= TRUE+1
    elif char in ['l','o','v','e']:
        LOVE=LOVE+1

score= int(str(TRUE)+str(LOVE))

if score<10 or score>90:
    print(f"Love score: {score}, you go together like coke and mentos.")
elif 40<score<50:
    print(f"Love score: {score}, you are alright together.")
else:
    print(f"Love score: {score}, you still have a chance together.")

