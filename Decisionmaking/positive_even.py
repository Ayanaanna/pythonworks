# wap to check whether the given number is positive even

# num=int(input("enter a number"))

# if num>0 and num%2==0:
#     print("positive even")
# else:
#     print("not positive")


# wap to check the bike tax
# if price of bike is above 1000000 add  tex is 12% along with price to total
# if the price of the bike is above or equal to 50k and
# less than or equal to 100000 and add tax of 7 % 
# if the price is below 50k add 5 % tax to it
price=int(input("enter price of bike"))
if price >100000:
    tax=12*price/100
    print(f"tax is {price+tax}")
elif price>=50000 and price<=100000:
    tax=7*price/100
    print(f"tax is {price +tax}")
else:
    tax=5*price/100
   
    print(f"tax is {tax+price}")