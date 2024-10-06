"""
Under 18.5 they are underweight
 Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
 Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""

#Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters e.g., 1.55\n"))
#Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms e.g., 72\n"))
#BMI= weight/(height^2)
bmi= weight/(height*height)

if bmi<18.5:
    print(f"Your BMI: {bmi}, You are underweight")
elif 18.5<bmi<25:
    print(f"Your BMI: {bmi}, You are normal weight")   
elif 25<bmi<30:
    print(f"Your BMI: {bmi}, You are slightly overweight")   
elif 30<bmi<35:
    print(f"Your BMI: {bmi}, You are obese") 
else:  
    print(f"Your BMI: {bmi}, You are clinically obese.") 