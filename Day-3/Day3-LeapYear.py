"""
A leap year is exactly divisible by 4 except for century years (years ending with 00). 
The century year is a leap year only if it is perfectly divisible by 400.
e.g. The year 2000:
 2000 : 4 = 500 (Leap)
 2000 : 100 = 20 (Not Leap)
 2000 : 400 == (Leap!)
So the year 2000 is a leap year.
But the year 2100 is not a leap year because:
 2100 : 4= 525 (Leap)
 2100 : 100 = 21 (Not Leap)
 2100 : 400 = 5.25 (Not Leap)
"""
# Which year do you want to check?
year = int(input("Which year do you want to check?\n"))

if (year%4==0) and (year%100!=0):
    print(f"The year {year} is a leap year")
elif (year%4==0) and (year%100==0) and (year%400==0):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")