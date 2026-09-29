# write a program to get bmi

# BMI=weight (kg)/[height (m)

weight=int(input('enter weight in kg'))
height=float(input("enter the height"))

bmi=weight/(height**2)
print(f"bmi is {bmi}")