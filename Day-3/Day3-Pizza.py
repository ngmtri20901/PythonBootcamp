"""""
Small pizza (S): S15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""""
size=input("What size pizza do you want? S, м, or L\n").upper()
add_pepperoni= input("Do you want pepperoni? Y or N\n").upper()
extra_cheese= input("Do you want extra cheese? Y or N\n").upper()

price=0

if size=="S":
    price=price + 15
elif size=="M":
    price=price + 20
elif size=="L":
    price=price + 25
else:
    print("Incorrect type, enter again")
    exit() 

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3
elif add_pepperoni != "N":
    print("Incorrect type, enter again")
    exit()

if extra_cheese=="Y":
   price=price+1
elif extra_cheese != "N":
    print("Incorrect type, enter again")
    exit()

print(f"Your bill: {price}")


