# bmr=(10 x weight in kg)+ (6.25 * height in cm)-(5 * age in years)+5
# ========================================

age=int(input("enter age"))
w=int(input("enter weight in kg"))
h=float(input("enter height in cm"))
# text{BMI} = \text{weight (kg)} / [\text{height (m)}]^2\)

BMI=w/h**2
if BMI<18.5:
    print(f"{BMI} underweight")
elif BMI>=18.5 and BMI<24.9:
    print(f"{BMI} normal")
elif BMI >25.0 and BMI<29.9:
    print(f"{BMI} overwight")
else:
    print(F"{BMI} obesity")
