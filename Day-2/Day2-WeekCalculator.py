age= input("Enter your age\n")
# presume that you live to 90 year old
# 90-age=age_left
#age_left * 365=days 
# days/7=weeks
age_left= 90- int(age)

days= int(age_left) * 365
weeks= int(days)//7  

print(f"You have {weeks} weeks left")