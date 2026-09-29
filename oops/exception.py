# # # sum of numbers
# # # try:
# # #     num1=int(input("enter number"))
# # #     num2=int(input("enter second number"))
# # #     s=num1+num2
# # #     print(s)
# # # except:
# # #     print("invalid number")
# # # else:
# # #     print("sum",s)
# # # finally:
# # #     print("done")


# # try:
# #     num1=int(input("enter number"))
# #     num2=int(input("enter second number"))
# #     s=num1/num2
# #     print(s)
# # except ZeroDivisionError:
# #     print("zero divsion error")
# # except ValueError:
# #     print("value error")
# # except:
# #     print("eroor")
# # else:
# #     print("sum",s)
# # finally:
# #     print("done")


# # import math

# # while True:
# #     try:
# #          n = int(input("Enter a number: "))
# #          print("Factorial =", math.factorial(n))
# #          break

   
# #     except ValueError:
# #         print("Invalid input. Please enter a number.")

       
# # while (True):
# #     try:
# #         print("1. Addition")
# #         print("2. Subtraction")
# #         print("3. Multiplication")
# #         print("4. Division")
    

# #         ch = int(input("Enter your choice: "))
# #         if ch in [1,2,3,4]:
# #             a = float(input("Enter first number: "))
# #             b = float(input("Enter second number: "))

# #             sum=a+b
# #             diff=a-b
# #             mul=a*b
# #             div=a/b

# #     except ValueError:
# #         print("Invalid input. Please enter numbers.")

# #     except ZeroDivisionError:
# #         print("Cannot divide by zero.")

# #     else:
# #         if ch == 1:
# #             print("Result =", a + b)

# #         elif ch == 2:
# #             print("Result =", a - b)

# #         elif ch == 3:
# #             print("Result =", a * b)

# #         elif ch == 4:
# #             print("Result =", a / b)

# #         else:
# #             exit()



# # try:
# #     filename = input("Enter file name: ")

# #     f = open(filename, "r")
# #     content = f.read()

# #     print(content)

# #     f.close()

# # except FileNotFoundError:
# #     print("File does not exist.")


# # d = {"name": "arun", "age": 23, "place": "ekm"}

# # try:
# #     key = input("Enter key: ")
# #     print("Value =", d[key])

# # except KeyError:
# #     print("Key does not exist.")

# try:
#     n=int(input("enter num 1"))
#     m=int(input("enter num2"))
#     r=n/m
#     print(r)

# except ValueError as s:
#     print(s)
#     print(type(s))
# except ZeroDivisionError as e:
#     print(e)

# except Exception as e:
#     print(e)

#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"

# try:
#     n=int(input("enter number"))
#     if (n<=0):
#         raise ValueError("number must be positive")

#     else:
#         print(n)
# except ValueError as e:
#     print(e)


#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8 
# characters")

# class InvalidPasswordError(Exception):
#     pass
# try:
#     n=input("Enter the password with 8 characters: ")
#     if len(n)<8:
#         raise InvalidPasswordError("The password should have 8 characters")
#     else:
#         print(n)
# except Exception as e:
#     print(e)

     


#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

class InsuffientBalanceError(Exception):
    pass
try:
    amount=int(input("Enter amount: "))
    balance=int(input("Enter balance: "))
    if amount>balance:
        raise InsuffientBalanceError("Not Enough Balance.Transaction Failed")
    else:
        print("Transaction Successfull")
except Exception as e: 
    print(e)
