# decision making
# =======================
# write a program to check whether a student is passed

# condition
# marks>=35 > pass
# otherwise > fail

# display the bonus percentage

# salary            bonus
# 500000              20%
# 300000              10%
# below 300000        5%

# marks=int(input("enter marks"))
# if marks>=35:
#     print("pass")
# else:
#     print("fail")

salary=int(input("enter salary"))
if salary==50000:
    bonus=salary*20/100
    print(f'total salary is {salary+bonus}')
elif salary ==30000:
      bonus=salary*20/100

      print(f"bonus is {salary+bonus}")

elif salary<30000:
    bonus=salary*5/100
    print(f"bonus is {salary +bonus}")
else:
     print("thankyou")